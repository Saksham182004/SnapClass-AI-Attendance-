import streamlit as st
import segno
import io

@st.dialog("Share class Link")
def share_subject_dialog(subject_name, subject_code):
    app_domain = "snapclass-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=10, border=2, dark='#5865F2', light='#ffffff')

    st.html(f"""
    <div style="text-align:center; margin-bottom:16px;">
        <span style="
            background: linear-gradient(135deg,#5865F2,#EB459E);
            color:white;
            padding: 6px 18px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.5px;
        ">{subject_name} &nbsp;·&nbsp; {subject_code}</span>
    </div>
    """)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.html("""
        <p style="color:#64748b; font-size:0.8rem; font-weight:600;
                  letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">
            Join URL
        </p>
        """)
        st.code(join_url, language="text")

        st.html("""
        <p style="color:#64748b; font-size:0.8rem; font-weight:600;
                  letter-spacing:1px; text-transform:uppercase; margin:12px 0 8px;">
            Subject Code
        </p>
        """)
        st.html(f"""
        <div style="
            background: linear-gradient(135deg,#E0E3FF,#f3f0ff);
            border: 2px dashed #5865F2;
            border-radius: 14px;
            padding: 16px;
            text-align: center;
            font-size: 1.8rem;
            font-weight: 800;
            color: #5865F2;
            letter-spacing: 4px;
        ">{subject_code}</div>
        """)

        st.html("""
        <p style="color:#94a3b8; font-size:0.78rem; margin-top:10px; text-align:center;">
            Share this code or link via WhatsApp, Email or QR
        </p>
        """)

    with col2:
        st.html("""
        <p style="color:#64748b; font-size:0.8rem; font-weight:600;
                  letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">
            Scan to join
        </p>
        """)
        st.image(out.getvalue(), use_container_width=True)
