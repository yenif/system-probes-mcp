import os
import json
import sys
import psutil

def ps(session_id=None):
    """Lists processes, optionally filtered by session ID."""
    try:
        processes = []
        for p in psutil.process_iter(['pid', 'name', 'username', 'status', 'cpu_percent', 'memory_percent']):
            try:
                p_info = p.info
                # Placeholder for session filtering
                processes.append(p_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return {'status': 'success', 'data': processes}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def status(pid):
    """Gets the detailed status of a specific process."""
    try:
        p = psutil.Process(pid)
        return {'status': 'success', 'data': {
            'pid': p.pid,
            'name': p.name(),
            'status': p.status(),
            'cpu_times': p.cpu_times(),
            'memory_info': p.memory_info(),
            'open_files': [f.path for f in p.open_files()],
            'connections': [c.laddr for c in p.connections()]
        }}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def get_proc_output(pid):
    """Retrieves the standard output and standard error streams of a running process."""
    # This is a complex feature to implement correctly and safely, as it requires
    # intercepting the process's output streams. For now, this is a placeholder.
    return {'status': 'error', 'message': 'get_proc_output is not yet implemented.'}

def main():
    """Main loop to process commands."""
    for line in sys.stdin:
        try:
            command = json.loads(line)
            action = command.get('action')
            args = command.get('args', {})

            if action == 'ps':
                result = ps(**args)
            elif action == 'status':
                result = status(**args)
            elif action == 'get_proc_output':
                result = get_proc_output(**args)
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
