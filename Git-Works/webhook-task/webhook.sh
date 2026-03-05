echo "Webhook triggered at $(date)" >> webhook.log

cd /var/www/mywebsite

git pull origin main
