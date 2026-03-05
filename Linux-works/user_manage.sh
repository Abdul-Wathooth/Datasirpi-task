useradd -m employee
echo "employee:Data@123" | chpasswd
usermod -aG sudo employee

echo "User created successfully."
