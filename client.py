from ftplib import FTP

def connect_ftp(host, username, password):
    try:
        ftp = FTP(host)
        ftp.login(user=username, passwd=password)
        print(f"✅ Connected to {host}")
        return ftp
    except Exception as e:
        print(f"❌ Failed to connect: {e}")
        return None

def list_files(ftp):
    print("📂 Files on the server:")
    ftp.retrlines('LIST')

def upload_file(ftp, local_file, remote_file):
    try:
        with open(local_file, 'rb') as f:
            ftp.storbinary(f'STOR {remote_file}', f)
        print(f"⬆️ Uploaded {local_file} to {remote_file}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")

def download_file(ftp, remote_file, local_file):
    try:
        with open(local_file, 'wb') as f:
            ftp.retrbinary(f'RETR {remote_file}', f.write)
        print(f"⬇️ Downloaded {remote_file} to {local_file}")
    except Exception as e:
        print(f"❌ Download failed: {e}")

def close_connection(ftp):
    ftp.quit()
    print("🔌 Connection closed.")

def main():
    host = input("FTP Host: ")
    username = input("Username: ")
    password = input("Password: ")

    ftp = connect_ftp(host, username, password)
    if not ftp:
        return

    while True:
        print("\nOptions:")
        print("1. List files")
        print("2. Upload file")
        print("3. Download file")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            list_files(ftp)
        elif choice == '2':
            local = input("Local file path: ")
            remote = input("Remote file name: ")
            upload_file(ftp, local, remote)
        elif choice == '3':
            remote = input("Remote file name: ")
            local = input("Local file path to save: ")
            download_file(ftp, remote, local)
        elif choice == '4':
            close_connection(ftp)
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()



