import streamlit as st
from streamlit_elements_fluence import elements, mui, JSCallback, extras

st.session_state.mui_license = "a license that was purchased from https://mui.com/r/x-get-license"

columns = [
    {"field": "id", "headerName": "ID", "width": 90},
    {"field": "firstName", "headerName": "First name", "width": 150, "editable": True},
    {
        "field": "lastName",
        "headerName": "Last name",
        "width": 150,
        "editable": True,
        "valueFormatter": JSCallback("""(params) => {return params.value ? params.value.toUpperCase() : ''}"""),
    },
]

rows = [
    {"id": 1, "lastName": "Snow", "firstName": "Jon"},
    {"id": 2, "lastName": "Lannister", "firstName": "Cersei"},
    {"id": 3, "lastName": "Lannister", "firstName": "Jaime"},
]

with elements("an_example"):

    mui.DataGridPro(
        columns=columns,
        rows=rows,
        autoHeight=True,
        components={
            "Toolbar": mui.GridToolbar(direct=True),
        },
    )

    mui.Typography("Click me!", onClick=JSCallback("""(params) => {alert('Clicked!')}"""))

    extras.InnerHTML(html="""<div onClick="alert('Clicked!')"<b>Click me!</b></div>""")
