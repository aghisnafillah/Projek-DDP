import streamlit as st

# CSS to Streamlit 
st.markdown(
    """
    <style>
    /* Warna latar belakang aplikasi */
    .stApp {
        background-color:  #A5B68D;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #EDE8DC;
        color: white;
        padding: 5px;
    }

    /* Teks pada sidebar */
    [data-testid="stSidebar"] * {
        color: black !important;
        font-size: 16px;
        margin-bottom: 5px;
        margin-top: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


Tentang = st.Page("./fitur/Tentang.py", title="🖊️Tentang")
To_Do_List = st.Page("./fitur/To Do List.py", title="📋To Do List")
Catatan_Baru = st.Page("./fitur/Catatan Baru.py", title="📖Catatan Baru")
Keuangan = st.Page("./fitur/Keuangan.py", title= "💰Keuangan")
Riwayat = st.Page("./fitur/Riwayat.py", title= "📜Riwayat")



pg = st.navigation(
    {
        
        "Menu Utama" : [Tentang, To_Do_List, Catatan_Baru, Keuangan, Riwayat]
        
            }
) 



if "total_semua" not in st.session_state:
    st.session_state["total_semua"] = []

pg.run()


