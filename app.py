import streamlit as st

st.title("Servidor Web")

st.header("Disciplina: Servidores e Computação em Nuvem")

st.write("Linguagem: Python.")
st.write("Os softwares: Python, Streamlit, GitHub.")
st.write("Aluno: Vitor Hugo Passos Ramalho.")
st.write(Turma: 2026.1)

nome = st.text_input("Digite seu nome:")

if nome:
    st.write("Olá,", “nome, "! O servidor está funcionando.")
