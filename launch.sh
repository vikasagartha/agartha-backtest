APP=${1:-agartha-backtest}

tmux new-session -d -s $APP
tmux new-window -t $APP:1

tmux select-window -t $APP:1
tmux split-window -h -p 75
tmux select-pane -L
tmux send-keys 'cd ./charts; http-server' C-m
tmux select-pane -R

tmux attach -t $APP
