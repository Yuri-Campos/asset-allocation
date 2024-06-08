import streamlit as st

st.set_page_config(
    page_title="Asset List",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded",
)

col1,col2,col3, col4, col5 = st.columns(5)
col3.markdown('# Asset List')
st.sidebar.markdown('Made by [Yuri Campos](https://github.com/Yuri-Campos)')


st.selectbox('Asset', ['asset1', 'asset2', 'asset3'])

st.markdown('## Asset 1')

st.markdown(f'**Position:** $200.00')
st.markdown(f'**%:** 40')
st.markdown(f'**size:** 42%')
st.markdown(f'**rebalance needed**: yes')
st.markdown(f'**rebalance**: sell $4.00' )


st.subheader(f'Wallet %')
col1,col2 = st.columns(2)
col1.progress(int(40))
col2.markdown('### 40%')