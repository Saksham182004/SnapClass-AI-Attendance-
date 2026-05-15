import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    
    html = f"""
    <div style="
        background: linear-gradient(135deg, #ffffff 60%, #f3f0ff 100%);
        border-radius: 20px;
        padding: 28px 30px 22px 30px;
        margin-bottom: 20px;
        box-shadow: 0 4px 24px rgba(88,101,242,0.10);
        border: 1.5px solid #E0E3FF;
        position: relative;
        overflow: hidden;
    ">
        <div style="
            position:absolute; top:0; left:0;
            width:8px; height:100%;
            background: linear-gradient(180deg, #EB459E, #5865F2);
            border-radius: 20px 0 0 20px;
        "></div>

        <h3 style="margin:0 0 6px 0; color:#1e293b; font-size:1.5rem; font-weight:700; letter-spacing:-0.5px;">
            {name}
        </h3>

        <p style="color:#64748b; margin:0 0 16px 0; font-size:0.95rem; display:flex; align-items:center; gap:10px;">
            <span style="background:#E0E3FF; color:#5865F2; padding:3px 10px; border-radius:6px; font-weight:600; font-size:0.85rem;">
                {code}
            </span>
            <span style="color:#94a3b8;">•</span>
            Section <b style="color:#1e293b;">{section}</b>
        </p>
    """

    if stats:
        html += """<div style="display:flex; gap:10px; flex-wrap:wrap;">"""

        for icon, label, value in stats:
            html += f'''
            <div style="
                background: linear-gradient(135deg, #EB459E, #c2185b);
                color: white;
                padding: 8px 16px;
                border-radius: 14px;
                font-size: 0.88rem;
                font-weight: 600;
                display: flex;
                align-items: center;
                gap: 6px;
                box-shadow: 0 2px 8px rgba(235,69,158,0.25);
            ">
                {icon} <span>{value}</span> <span style="opacity:0.85; font-weight:400;">{label}</span>
            </div>
            '''

        html += "</div>"

    html += "</div>"

    st.html(html)

    if footer_callback:
        footer_callback()