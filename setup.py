from cx_Freeze import setup, Executable

setup(
    name="DivoTech",
    version="1.0",
    description="Divo Tech é o meu assistente pessoal.",
    executables=[Executable("assistente.py")]
)
