#!/usr/bin/env zsh

pushd /Users/rudy/code/neurocards/server
source ".venv/bin/activate"
python /Users/rudy/code/neurocards/server/app.py &
deactivate
popd

# Kill the webserver
# pkill -f "python.*app.py"
