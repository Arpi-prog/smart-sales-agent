import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import streamlit as st
from tenacity import retry, stop_after_attempt, wait_fixed
import re
from datetime import datetime

class EmailSender:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.context = ssl.create_default_context()
    
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def send_email(self, sender_email, sender_password, recipient_email, subject, body):
        """Send email with retry logic and proper error handling"""
        try:
            # Validate inputs
            if not all([sender_email, sender_password, recipient_email, subject, body]):
                raise ValueError("All email fields are required")
            
            if not self.validate_email_format(sender_email):
                raise ValueError("Invalid sender email format")
                
            if not self.validate_email_format(recipient_email):
                raise ValueError("Invalid recipient email format")

            # Create message
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=self.context)
                server.login(sender_email, sender_password)
                server.send_message(message)
                
            return True
            
        except smtplib.SMTPAuthenticationError:
            raise Exception("Authentication failed. Check your email and app password.")
        except smtplib.SMTPRecipientsRefused:
            raise Exception("Recipient email refused. Please check the address.")
        except smtplib.SMTPServerDisconnected:
            raise Exception("Server disconnected. Please try again.")
        except Exception as e:
            raise Exception(f"Failed to send email: {str(e)}")

    @staticmethod
    def validate_email_format(email):
        """Validate email format using regex"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def test_connection(self, sender_email, sender_password):
        """Test SMTP connection without sending email"""
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=self.context)
                server.login(sender_email, sender_password)
            return True
        except Exception as e:
            st.error(f"Connection test failed: {str(e)}")
            return False

def send_email_ui(sender_email, sender_password, recipient_email, subject, body):
    """Streamlit UI wrapper for sending emails with session state management"""
    if not all([sender_email, sender_password, recipient_email]):
        st.error("Please configure email settings in the sidebar")
        return False
    
    status = st.empty()
    status.info("🔄 Sending email...")
    
    try:
        # Initialize email sender
        sender = EmailSender()
        
        # Send email
        sender.send_email(
            sender_email=sender_email,
            sender_password=sender_password,
            recipient_email=recipient_email,
            subject=subject,
            body=body
        )
        status.success("✅ Email sent successfully!")
        
        # Initialize sent_emails if not exists
        if 'sent_emails' not in st.session_state:
            st.session_state.sent_emails = []
            
        # Record sent email
        st.session_state.sent_emails.append({
            'to': recipient_email,
            'subject': subject,
            'time': datetime.now().strftime("%H:%M:%S"),
            'status': 'success'
        })
        
        return True
        
    except Exception as e:
        status.error(f"❌ Failed to send email: {str(e)}")
        
        # Record failed attempt
        if 'sent_emails' not in st.session_state:
            st.session_state.sent_emails = []
            
        st.session_state.sent_emails.append({
            'to': recipient_email,
            'subject': subject,
            'time': datetime.now().strftime("%H:%M:%S"),
            'status': 'failed',
            'error': str(e)
        })
        
        # Show troubleshooting
        st.error("""
        🔧 Troubleshooting Tips:
        1. Use an App Password (not your regular password)
        2. Enable 2FA in your Google account
        3. Check if Google blocked the attempt (visit security.google.com)
        4. Try a different network
        5. Verify recipient email format
        """)
        return False

# Helper function for displaying email history
def show_email_history():
    """Display sent emails from session state"""
    if 'sent_emails' in st.session_state and st.session_state.sent_emails:
        st.subheader("📨 Email History")
        for i, email in enumerate(reversed(st.session_state.sent_emails)):
            status_color = "#4CAF50" if email.get('status') == 'success' else "#F44336"
            st.markdown(f"""
            <div style="border-left: 3px solid {status_color}; 
                        padding: 8px 12px; 
                        margin: 8px 0;
                        background-color: #f8f9fa;
                        border-radius: 4px;">
                <div style="font-size: 0.8em; color: #666;">{email['time']}</div>
                <div><strong>To:</strong> {email['to']}</div>
                <div><strong>Subject:</strong> {email['subject']}</div>
                {f"<div style='color: {status_color};'><strong>Status:</strong> {email['status'].title()}</div>"}
                {f"<div style='color: #F44336;'><strong>Error:</strong> {email.get('error', '')}</div>" if email.get('error') else ""}
            </div>
            """, unsafe_allow_html=True)