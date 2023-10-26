from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="APP",
    settings_file=["settings.toml", ".secrets.toml"],
    eviroments=["development", "production"],
    env_switcher="APP_ENVIROMENT",
)
