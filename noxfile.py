import nox

nox.options.default_venv_backend = "uv"


@nox.session()
def show_poly_info(session: nox.Session):
    session.install("polylith-cli")
    session.run("poly", "info")


@nox.session()
def poly_sync(session: nox.Session):
    session.install("polylith-cli")
    session.run("poly", "sync")


@nox.session()
def typecheck(session: nox.Session):
    session.install("pyright")
    session.install("nox")
    session.run("pyright", *session.posargs)


@nox.session
def lint(session: nox.Session):
    """
    Lint the project using ruff.
    """
    session.install("ruff")
    session.run("ruff", "check", *session.posargs)


@nox.session
def autoformat(session: nox.Session):
    """
    Autoformat the project using ruff.
    """
    session.install("ruff")
    session.run("ruff", "format", *session.posargs)


@nox.session(default=False)
def full_test(session: nox.Session):
    """
    Run the test suite.
    """
    session.install("pytest", "coverage", "pytest-cov")
    session.install(".")
    session.run("pytest", "test/")


@nox.session(default=False)
def diff_test(session: nox.Session):
    session.install("polylith-cli", "pytest", "coverage", "pytest-cov", ".")
    result = session.run("poly", "diff", "--since", "release", "--short", "--bricks", silent=True)

    if not isinstance(result, str):
        session.error("Failed to run poly diff")

    changed_bricks = result.strip().split(",")

    session.run("pytest", "-k", " or ".join(changed_bricks), "test/")
