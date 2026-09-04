@echo off
title SIH26044 Public Live Tunnel
echo ========================================================
echo Starting Cloudflare Tunnel for SIH26044 Portal...
echo ========================================================
echo This window keeps your public internet link active!
echo Leave this window open while presenting or sharing.
echo ========================================================
"C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel --url http://127.0.0.1:8000
pause
