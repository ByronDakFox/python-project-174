def format_plain(diff, path=''):
    lines = []

    for node in diff:
        key = node['key']
        full_path = f"{path}.{key}" if path else key
        status = node['status']
        
