from pathlib import Path

import pytest

from starbot.pytest.cog_manager import *
from starbot.core import _cog_manager


@pytest.mark.skip
async def test_ensure_cogs_in_paths(cog_mgr, default_dir):
    cogs_dir = default_dir / "starbot" / "cogs"
    assert cogs_dir in await cog_mgr.paths()


async def test_install_path_set(cog_mgr: _cog_manager.CogManager, tmpdir):
    path = Path(str(tmpdir))
    await cog_mgr.set_install_path(path)
    assert await cog_mgr.install_path() == path


async def test_install_path_set_bad(cog_mgr):
    path = Path("something")

    with pytest.raises(ValueError):
        await cog_mgr.set_install_path(path)


async def test_add_path(cog_mgr, tmpdir):
    path = Path(str(tmpdir))
    await cog_mgr.add_path(path)
    assert path in await cog_mgr.paths()


async def test_add_path_already_install_path(cog_mgr, tmpdir):
    path = Path(str(tmpdir))
    await cog_mgr.set_install_path(path)
    with pytest.raises(ValueError):
        await cog_mgr.add_path(path)


async def test_remove_path(cog_mgr, tmpdir):
    path = Path(str(tmpdir))
    await cog_mgr.add_path(path)
    await cog_mgr.remove_path(path)
    assert path not in await cog_mgr.paths()
