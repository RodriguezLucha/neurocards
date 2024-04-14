#!/bin/bash

sleep 3

pushd /Users/rudy/code/neurocards/server
source ".venv/bin/activate"
python /Users/rudy/code/neurocards/server/app.py &
deactivate
popd

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"                   # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_completion

pushd /Users/rudy/code/neurocards/frontend/study
npx serve -s build -l 3006 &
popd

# Kill the webserver
# pkill -f "node.*start.js"
# pkill -f "python.*app.py"
