from IPython.display import display, HTML


def show_output(title: str, content: str, background: str = "#f5f5f5", text_color: str = "#333333") -> None:
    html = f"""
    <div style="background-color: {background}; padding: 15px; border-radius: 8px; margin: 10px 0;">
        <h3 style="color: {text_color}; margin-top: 0;">{title}</h3>
        <pre style="color: {text_color}; white-space: pre-wrap; word-wrap: break-word;">{content}</pre>
    </div>
    """
    display(HTML(html))
