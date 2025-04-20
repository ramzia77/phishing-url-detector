import re
from urllib.parse import urlparse
import tldextract
import pandas as pd

def extract_features(url):
    # Define all expected features here
    feature_names = [
        'length_url', 'length_hostname', 'domain_length',
        'nb_dots', 'nb_hyphens', 'nb_at', 'nb_qm', 'nb_and', 'nb_or',
        'nb_eq', 'nb_underscore', 'nb_percent', 'nb_slash', 'nb_star',
        'nb_colon', 'nb_comma', 'nb_semicolumn', 'nb_dollar', 'nb_space',
        'nb_www', 'nb_com', 'nb_dslash',
        'ip', 'https', 'prefix_suffix', 'short_url'
    ]

    features = dict.fromkeys(feature_names, 0)  # Default 0 for all

    try:
        parsed = urlparse(url)
        ext = tldextract.extract(url)

        hostname = parsed.hostname or ''
        domain = ext.domain + '.' + ext.suffix if ext.suffix else ext.domain

        features['length_url'] = len(url)
        features['length_hostname'] = len(hostname)
        features['domain_length'] = len(domain)

        # Count special characters
        features['nb_dots'] = url.count('.')
        features['nb_hyphens'] = url.count('-')
        features['nb_at'] = url.count('@')
        features['nb_qm'] = url.count('?')
        features['nb_and'] = url.count('&')
        features['nb_or'] = url.count('|')
        features['nb_eq'] = url.count('=')
        features['nb_underscore'] = url.count('_')
        features['nb_percent'] = url.count('%')
        features['nb_slash'] = url.count('/')
        features['nb_star'] = url.count('*')
        features['nb_colon'] = url.count(':')
        features['nb_comma'] = url.count(',')
        features['nb_semicolumn'] = url.count(';')
        features['nb_dollar'] = url.count('$')
        features['nb_space'] = url.count(' ')
        features['nb_www'] = url.count('www')
        features['nb_com'] = url.count('.com')
        features['nb_dslash'] = url.count('//')

        # IP address in URL?
        features['ip'] = 1 if re.search(r'(([0-9]{1,3}\.){3}[0-9]{1,3})', url) else 0

        # HTTPS or not
        features['https'] = 1 if parsed.scheme == 'https' else 0

        # Hyphen in domain
        features['prefix_suffix'] = 1 if '-' in domain else 0

        # URL shorteners
        shortening_services = (
            r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|tinyurl|tr\.im|is\.gd|"
            r"cli\.gs|yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|"
            r"twurl\.nl|snipurl\.com|short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|"
            r"bkite\.com|snipr\.com|fic\.kr|loopt\.us|doiop\.com|short\.ie|kl\.am|wp\.me|"
            r"rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|qr\.ae|adf\.ly|"
            r"bitly\.com|cur\.lv|ity\.im|q\.gs|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|"
            r"buzurl\.com|cutt\.us|u\.bb|yourls\.org|xzb\.cc|v\.gd|tr\.im|link\.zip\.net"
        )
        features['short_url'] = 1 if re.search(shortening_services, url) else 0

    except Exception as e:
        print(f"❌ Error extracting features from URL '{url}': {e}")
        # Still return full DataFrame with default values

    return pd.DataFrame([features])  # Always 1 row, all expected columns



