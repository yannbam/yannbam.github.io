#!/bin/bash
# Croissant viewer launcher

echo "🥐 Three.js Croissant Viewer"
echo "=========================="
echo ""
echo "Choose how to view:"
echo "1) Gallery - All demos overview"
echo "2) Interactive - Parameter sliders"
echo "3) Advanced - Full explorer"
echo "4) Via web server (ES6 modules)"
echo "5) Direct file (standalone)"
echo ""
read -p "Your choice (1-5): " choice

case $choice in
    1)
        echo "Opening gallery..."
        xdg-open ~/project/croissant/gallery.html 2>/dev/null || open ~/project/croissant/gallery.html 2>/dev/null
        ;;
    2)
        echo "Opening interactive explorer..."
        xdg-open ~/project/croissant/interactive.html 2>/dev/null || open ~/project/croissant/interactive.html 2>/dev/null
        ;;
    3)
        echo "Opening advanced explorer..."
        xdg-open ~/project/croissant/advanced.html 2>/dev/null || open ~/project/croissant/advanced.html 2>/dev/null
        ;;
    4)
        echo "Starting web server..."
        cd ~/project/croissant
        python3 -m http.server 8080 &
        SERVER_PID=$!
        sleep 1
        echo "Opening http://localhost:8080 in browser..."
        xdg-open http://localhost:8080 2>/dev/null || open http://localhost:8080 2>/dev/null
        echo ""
        echo "Server running with PID $SERVER_PID"
        echo "Press Ctrl+C to stop the server"
        wait $SERVER_PID
        ;;
    5)
        echo "Opening standalone version..."
        xdg-open ~/project/croissant/standalone.html 2>/dev/null || open ~/project/croissant/standalone.html 2>/dev/null
        ;;
    *)
        echo "Invalid choice"
        ;;
esac