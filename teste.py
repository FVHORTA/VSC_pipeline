import streamlit as st
from datetime import datetime, time

def main():
    st.title('Title')
    nome = st.text_input('Nome')
    idade = st.number_input('Idade',max_value=120)
    data = st.date_input('Data', value=datetime.now(), min_value=datetime(1920, 12, 1)).strftime('%d/%m/%Y')
    dataf = data.strftime('%d/%m/%Y')
    status = st.selectbox('Status', ['S', 'N' ])
    hora_atual = st.time_input ('Hora')
    email = st.text_input('E-mail')
    st.write(f'Hora atual: {hora_atual}')

    if st.button('Salvar'):
        st.write('Cadastrado:')
        st.write(f'Nome: {nome}')
        st.write(f'Idade: {idade}')
        st.write(f'Status: {status}')
        st.write(f'Data: {dataf}')
        st.write(f'Hora: {hora_atual}')
        data_hora = datetime.combine(data, hora_atual)
        st.write(f'Data-Hora: {data_hora}')
        st.write(f'E-mail: {email}')
        




if __name__ == '__main__':

    main()

#principal