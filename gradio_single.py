"""
Single-file launcher for the Gradio web UI.

This script acts as a single entrypoint to start the Gradio app defined in
`gradio_app.py`. It keeps the project layout intact (no code in tsr/ is
inlined) and simply adjusts Python's sys.path so `gradio_app` can be imported
from the project root. It then parses the same CLI flags used by
`gradio_app.py` and launches the `interface` object.

Usage (PowerShell):
    python gradio_single.py --port 7860
    python gradio_single.py --port 7860 --listen --share

Notes:
  - This is a convenience wrapper. Dependencies, model files, and native
    extensions still need to be installed in the environment.
  - Running this will import `gradio_app` which initializes the model and
    therefore may download the model weights on first run.
"""
import argparse
import os
import sys

# Ensure project root is on sys.path so `import gradio_app` works from anywhere
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', type=str, default=None, help='Username for authentication')
    parser.add_argument('--password', type=str, default=None, help='Password for authentication')
    parser.add_argument('--port', type=int, default=7860, help='Port to run the server listener on')
    parser.add_argument('--listen', action='store_true', help='launch gradio with 0.0.0.0 as server name, allowing to respond to network requests')
    parser.add_argument('--share', action='store_true', help='use share=True for gradio and make the UI accessible through their site')
    parser.add_argument('--queuesize', type=int, default=1, help='launch gradio queue max_size')
    args = parser.parse_args()

    # Import the Gradio app. This will construct `interface` and load the model.
    import gradio_app as app

    # Mirror the behavior in gradio_app.py's __main__ block
    app.interface.queue(max_size=args.queuesize)
    app.interface.launch(
        auth=(args.username, args.password) if (args.username and args.password) else None,
        share=args.share,
        server_name="0.0.0.0" if args.listen else None,
        server_port=args.port,
    )

if __name__ == '__main__':
    main()
