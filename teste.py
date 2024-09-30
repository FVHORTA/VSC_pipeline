import streamlit as st
from datetime import datetime
from contrato import cadastros
from pydantic import ValidationError


def main():
    st.title('Title')
    nome = st.text_input('Nome', max_chars=120).upper()
    idade = st.number_input('Idade', min_value=0, max_value=120, step=1, value=13, format='%d')
    data = st.date_input('Data', value=datetime.now(), min_value=datetime(1920, 12, 1))
    email = st.text_input('E-mail')
    status = st.selectbox('Status', ['Ativo', 'Inativo'])
    hora_atual = datetime.now().time()
    data_hora = datetime.combine(data, hora_atual).strftime('%Y-%m-%d %H:%M:%S')

    if st.button('Salvar'):
        try:
            cadastro = cadastros(nome=nome, idade=idade, data=data, email=email, status = status,  data_hora=data_hora)
        except ValidationError as e:
            st.error(str(e))
            return


        st.write('Cadastrado:')
        st.write(f'Nome: {nome}')
        st.write(f'Idade: {idade}')
        st.write(f'Status: {status}')
        st.write(f'Data-Hora: {data_hora}')
        st.write(f'E-mail: {email}')
        




if __name__ == '__main__':

    main()

