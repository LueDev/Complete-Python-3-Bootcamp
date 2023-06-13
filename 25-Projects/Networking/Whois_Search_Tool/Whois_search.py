import whois

def whois_lookup(domain):
    """Perform a WHOIS lookup for a domain."""
    try:
        pythonwhois = whois.whois(domain)
        if pythonwhois['status']:
            print(f"Domain: {pythonwhois['domain_name']}")
            print(f"Registrar: {pythonwhois['registrar']}")
            print(f"Creation date: {pythonwhois['creation_date']}")
            print(f"Expiration date: {pythonwhois['expiration_date']}")
            print(f"Registrant: {pythonwhois['registrant']}")
            print(f"Admin contact: {pythonwhois['admin_contact']}")
            print(f"Technical contact: {pythonwhois['technical_contact']}")
            print(f"Nameservers: {pythonwhois['name_servers']}")
        else:
            print("Error: WHOIS information not available for this domain")
    except Exception as e:
        print(e)

whois_lookup('papiluee.nyc')
