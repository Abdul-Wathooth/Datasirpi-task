useradd -m employee
echo "employer:Data@123" | chpasswd
usermod -aG sudo employee

echo "User created successfully."
