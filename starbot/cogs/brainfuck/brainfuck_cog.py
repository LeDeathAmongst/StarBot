import discord
import argparse
from starbot.core import commands
from Star-Utils import Cog
from .dashboard_integration import DashboardIntegration

class brainfuck(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["bf"])
    async def brainfuck(self, ctx, *, text: str):
        """
        Compiles normal text into Brainfuck code.        """
        try:
            code = self.compile_to_brainfuck(text)
            await ctx.send("Compiled Brainfuck code:\n```" + code + "```")
        except Exception as e:
            await ctx.send(f"Error: {e}")

    @commands.command(aliases=["ubf"])
    async def unbrainfuck(self, ctx, *, code: str):
        """
        Interprets Brainfuck code and converts it to normal text.        """
        try:
            result = self.run_brainfuck(code)
            await ctx.send("Decoded text:\n```" + result + "```")
        except Exception as e:
            await ctx.send(f"Error: {e}")
    def run_brainfuck(self, code):
        cells = [0] * 30000  # Initialize memory cells
        output = ""
        ptr = 0  # Pointer to current memory cell
        code_ptr = 0  # Pointer to current code instruction

        while code_ptr < len(code):
            command = code[code_ptr]

            if command == ">":
                ptr += 1
            elif command == "<":
                ptr -= 1
            elif command == "+":
                cells[ptr] = (cells[ptr] + 1) % 256
            elif command == "-":
                cells[ptr] = (cells[ptr] - 1) % 256
            elif command == ".":
                output += chr(cells[ptr])
            elif command == ",":
                pass  # You can implement input functionality here
            elif command == "[" and cells[ptr] == 0:
                loop_depth = 1
                while loop_depth > 0:
                    code_ptr += 1
                    if code[code_ptr] == "[":
                        loop_depth += 1
                    elif code[code_ptr] == "]":
                        loop_depth -= 1
            elif command == "]" and cells[ptr] != 0:
                loop_depth = 1
                while loop_depth > 0:
                    code_ptr -= 1
                    if code[code_ptr] == "[":
                        loop_depth -= 1
                    elif code[code_ptr] == "]":
                        loop_depth += 1

            code_ptr += 1

        return output

    def compile_to_brainfuck(self, text):
        parser = argparse.ArgumentParser(description='Text to Brainfuck generator.')
        parser.add_argument('--string', metavar='S', help='String to be printed by Brainfuck source code.')
        args = parser.parse_args(["--string", text])

        source_code = self.string_to_bf(args.string, False)

        return source_code

    def string_to_bf(self, string, commented):
        buffer = ""
        if string is None:
            return buffer
        for i, char in enumerate(string):
            if i == 0:
                buffer = buffer + self.char_to_bf(char)
            else:
                delta = ord(string[i]) - ord(string[i - 1])
                buffer = buffer + self.delta_to_bf(delta)
            if commented:
                buffer = buffer + ' ' + string[i].strip('+-<>[],.') + '\n'
        return buffer

    def char_to_bf(self, char):
        buffer = "[-]>[-]<"
        for i in range(ord(char)//10):
            buffer = buffer + "+"
        buffer = buffer + "[>++++++++++<-]>"
        for i in range(ord(char) % 10):
            buffer = buffer + "+"
        buffer = buffer + ".<"
        return buffer

    def delta_to_bf(self, delta):
        buffer = ""
        for i in range(abs(delta) // 10):
            buffer = buffer + "+"

        if delta > 0:
            buffer = buffer + "[>++++++++++<-]>"
        else:
            buffer = buffer + "[>----------<-]>"

        for i in range(abs(delta) % 10):
            if delta > 0:
                buffer = buffer + "+"
            else:
                buffer = buffer + "-"
        buffer = buffer + ".<"
        return buffer

def setup(bot):
    bot.add_cog(brainfuck(bot))