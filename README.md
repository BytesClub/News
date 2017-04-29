# News

[![gitter](https://badges.gitter.im/gitterHQ/gitterHQ.github.io.svg)](https://gitter.im/Bytes_Club/General)

A python script to download the current day's Telegraph newspaper in Portable Document Format (PDF)

### Requirements

1. Python
```
sudo apt-get install --reinstall python-gi
```

2. Requests

```
sudo pip install requests
```

3. BeautifulSoup4

```
sudo pip install BeautifulSoup4
```

### Usage

Run the script via:

```
python news.py [OPTIONS]
```

### OPTIONS
    -fp, --frontpage                       Download the frontpage
    -n, --nation                       Download the Nations page
    -f, --foreign                       Download the Foreign page
    -c, --calcutta                       Download the Calcutta page
    -b, --bengal                       Download the Bengal page
    -bsns, --business                       Download the Business page
    -s, --sports                       Download the Sports page

### Contribution

Read [contributions](https://bytesclub.github.io/contributing/)
