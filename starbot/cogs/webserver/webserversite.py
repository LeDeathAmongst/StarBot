import os
import logging
import signal
from flask import Flask, request, jsonify, render_template, abort, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix
import asyncio
import nacl.signing
import nacl.exceptions
import json
from hypercorn.config import Config
from asgiref.wsgi import WsgiToAsgi
import sentry_sdk
from hypercorn.asyncio import serve
sentry_sdk.init(dsn=None)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# Global variables to store configurations
bot = None
public_key = None
application_id = None

def setup_webserver(red_bot, port, pk, app_id):
    global bot, public_key, application_id
    bot = red_bot
    public_key = pk
    application_id = app_id

def verify_signature(signature: str, timestamp: str, body: str) -> bool:
    if not public_key:
        logger.error("Public key not set")
        return False
    try:
        verify_key = nacl.signing.VerifyKey(bytes.fromhex(public_key))
        verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
        return True
    except nacl.exceptions.BadSignatureError:
        return False

def get_changelogs():
    try:
        with open('changelogs.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/webhook', methods=['POST'])
def discord_webhook():
    logger.info("Received webhook request")

    signature = request.headers.get('X-Signature-Ed25519')
    timestamp = request.headers.get('X-Signature-Timestamp')

    if not verify_signature(signature, timestamp, request.data.decode('utf-8')):
        logger.warning("Failed signature verification")
        return '', 401

    payload = request.json
    logger.info(f"Received full payload:\n{json.dumps(payload, indent=2)}")

    if payload['type'] == 0:  # PING event
        logger.info("Received PING event. Responding with 204 No Content.")
        return '', 204

    elif payload['type'] == 1:
        logger.info("Received Event. Responding with 204 No Content.")
        return '', 204

    else:
        logger.warning(f"Unhandled payload type: {payload['type']}")
        logger.info("Responding with 400 Bad Request")
        return '', 400

@app.route('/help')
def help_page():
    # Path to the JSON file
    json_path = os.path.join(os.path.dirname(__file__), 'static', 'commands_data.json')

    # Read the JSON file
    with open(json_path, 'r') as file:
        commands_data = json.load(file)

    # Render the template with the commands data
    return render_template('help.html', commands=commands_data)

@app.route('/commands_data.json')
def commands_data():
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'static'), 'commands_data.json')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

@app.route('/webhook-logs')
def webhook_logs():
    if not bot:
        return jsonify({'error': 'Bot not ready'}), 503
    cog = bot.get_cog('WebServerCog')
    if not cog:
        return jsonify({'error': 'WebServerCog not loaded'}), 503
    bot_name = bot.user.name if bot.user else "Bot"
    bot_avatar = bot.user.avatar.url if bot.user and bot.user.avatar else ""
    return render_template('webhook_logs.html', logs=cog.log_entries, bot_name=bot_name, bot_avatar=bot_avatar)

@app.route('/webhook-logs-content')
def webhook_logs_content():
    if not bot:
        return jsonify({'error': 'Bot not ready'}), 503
    cog = bot.get_cog('WebServerCog')
    if not cog:
        return jsonify({'error': 'WebServerCog not loaded'}), 503
    return render_template('logs_content.html', logs=cog.log_entries)

@app.route('/bot-info')
def bot_info():
    if not bot:
        return jsonify({'error': 'Bot not ready'}), 503
    return jsonify({
        "name": bot.user.name if bot.user else "Bot",
        "avatar": bot.user.avatar.url if bot.user and bot.user.avatar else ""
    })

@app.route('/')
def invite_page():
    if not application_id:
        return jsonify({'error': 'Application ID not set'}), 503
    invite_links = {
        'Main Invite': f'https://discord.com/oauth2/authorize?client_id={application_id}&scope=bot%20applications.commands',
        'Admin Invite': f'https://discord.com/oauth2/authorize?client_id={application_id}&scope=bot%20applications.commands&permissions=8',
        'Support Server': 'https://discord.gg/your_support_server',
        'Basic Perms Invite': f'https://discord.com/oauth2/authorize?client_id={application_id}&scope=bot%20applications.commands&permissions=8'
    }
    return render_template('invite.html', invite_links=invite_links)

@app.route('/bot-stats')
async def bot_stats():
    if not bot:
        return jsonify({'error': 'Bot not ready'}), 503
    server_count = len(bot.guilds)
    user_count = sum(guild.member_count for guild in bot.guilds)
    logger.info(f"Returning stats: servers={server_count}, users={user_count}")
    return jsonify({
        'server_count': server_count,
        'user_count': user_count
    })

@app.route('/changelogs')
def changelogs():
    logs = get_changelogs()
    return render_template('changelogs.html', changelogs=logs)

@app.route('/changelogs/<version>')
def changelog_detail(version):
    logs = get_changelogs()
    for log in logs:
        if log['version'] == version:
            return render_template('changelog_detail.html', changelog=log)
    abort(404)

async def run_flask(port):
    config = Config()
    config.bind = [f"0.0.0.0:{port}"]
    await serve(app, config)

async def shutdown(loop, signal=None):
    if signal:
        logger.info(f"Received exit signal {signal.name}...")
    logger.info("Shutting down...")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()

def signal_handler(sig, frame):
    loop = asyncio.get_event_loop()
    loop.create_task(shutdown(loop, signal=sig))

def start_webserver(red_bot, port, pk, app_id):
    global bot, public_key, application_id
    bot = red_bot
    public_key = pk
    application_id = app_id

    loop = asyncio.get_event_loop()
    signals = (signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(s, lambda s=s: signal_handler(s, None))

    try:
        loop.run_until_complete(run_flask(port))
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt. Shutting down...")
    finally:
        loop.run_until_complete(shutdown(loop))
        logger.info("Successfully shut down the webserver.")

if __name__ == '__webserver__':
    # This is just for testing the webserver independently
    app.run(host='0.0.0.0', port=8000)
