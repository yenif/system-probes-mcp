import os
import json
import sys
import stat as stat_mode
import glob

def ls(path):
    """Lists the contents of a directory."""
    try:
        files = []
        for f in os.listdir(path):
            f_path = os.path.join(path, f)
            f_stat = os.stat(f_path)
            files.append({
                'name': f,
                'size': f_stat.st_size,
                'type': 'dir' if os.path.isdir(f_path) else 'file',
                'mode': stat_mode.filemode(f_stat.st_mode),
                'modified': f_stat.st_mtime
            })
        return {'status': 'success', 'data': files}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def cat(path, start_line=None, end_line=None):
    """Reads the content of a file."""
    try:
        with open(path, 'r') as f:
            lines = f.readlines()
        if start_line is not None and end_line is not None:
            return {'status': 'success', 'data': "".join(lines[start_line:end_line])}
        return {'status': 'success', 'data': "".join(lines)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def stat(path):
    """Retrieves detailed metadata about a file or directory."""
    try:
        f_stat = os.stat(path)
        return {'status': 'success', 'data': {
            'size': f_stat.st_size,
            'mode': stat_mode.filemode(f_stat.st_mode),
            'uid': f_stat.st_uid,
            'gid': f_stat.st_gid,
            'modified': f_stat.st_mtime,
            'created': f_stat.st_ctime
        }}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def find(path, name_pattern):
    """Searches for files and directories."""
    try:
        results = []
        for p in glob.glob(os.path.join(path, name_pattern), recursive=True):
            results.append(p)
        return {'status': 'success', 'data': results}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def main():
    """Main loop to process commands."""
    for line in sys.stdin:
        try:
            command = json.loads(line)
            action = command.get('action')
            args = command.get('args', {})

            if action == 'ls':
                result = ls(**args)
            elif action == 'cat':
                result = cat(**args)
            elif action == 'stat':
                result = stat(**args)
            elif action == 'find':
                result = find(**args)
            else:
                result = {'status': 'error', 'message': f'Unknown action: {action}'}

            print(json.dumps(result))
            sys.stdout.flush()
        except json.JSONDecodeError:
            print(json.dumps({'status': 'error', 'message': 'Invalid JSON input.'}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({'status': 'error', 'message': str(e)}))
            sys.stdout.flush()

if __name__ == '__main__':
    main()
