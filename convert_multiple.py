from weasyprint import HTML, default_url_fetcher
from weasyprint.fonts import FontConfiguration
from datetime import date
import yaml
import os
import ssl
import logging

def fetcher_timout(url, timeout=3600):
    return default_url_fetcher(url, timeout)

LOG_DIR = "/app/logs/"
DEST_DIR = "/app/output/"
CONFIG_DIR = "/app/config/"

logger = logging.getLogger('weasyprint')
logger.addHandler(logging.FileHandler(LOG_DIR + 'weasyprint.log'))
ssl._create_default_https_context = ssl._create_unverified_context

now = date.today()
date = now.strftime("%y%m%d")

font_config = FontConfiguration()

config_file = CONFIG_DIR + "config.yml"
with open(config_file) as file:
  config = yaml.load(file, Loader=yaml.FullLoader)

for name, html in config['html_files'].items():
  dest = DEST_DIR + date + '_salesmat_' + name + '.pdf'
  print("Generate " + html + " into " + dest)
  HTML(html, url_fetcher=fetcher_timout).write_pdf(dest, font_config=font_config)