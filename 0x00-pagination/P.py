import requests

def download_file(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

# Specify the URL of the CSV file and the destination file path
csv_url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240128%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240128T133236Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b03a77f3604a0afff7839212c2decd6f5933bdacdf4d7160bb3d9a21ddc1370b"
destination_path = "Popular_Baby_Names.csv"

# Download the file
download_file(csv_url, destination_path)
