# saunadge

![Build image](https://github.com/po3rin/saunadge/workflows/Build%20image/badge.svg)
[![PyPi version](https://img.shields.io/pypi/v/saunadge.svg)](https://pypi.python.org/pypi/saunadge/)
[![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)


saunadge lets you to generate sakatsu(サ活/サウナ活動) badge. saunadge server aggregates from the data over [SAUNA-IKITAI](https://sauna-ikitai.com/).

saunadge API moves anothor repository. CLI will continue to be managed in this repository.
https://github.com/po3rin/saunadge-rs

## Example

You can decide the badge style with `style` option.

[![sakatsu badge](https://img.shields.io/endpoint.svg?url=https://saunadge-gjqqouyuca-an.a.run.app/api/v1/badge/46531&style=for-the-badge)](https://sauna-ikitai.com/saunners/46531)
  
[![sakatsu badge](https://img.shields.io/endpoint.svg?url=https://saunadge-gjqqouyuca-an.a.run.app/api/v1/badge/46531&style=flat-square)](https://sauna-ikitai.com/saunners/46531)
  
[![sakatsu badge](https://img.shields.io/endpoint.svg?url=https://saunadge-gjqqouyuca-an.a.run.app/api/v1/badge/46531&style=flat)](https://sauna-ikitai.com/saunners/46531)

## Usage

First of all,  you must get sauna-ikitai-id.
<sauna-ikitai-id> can be obtained from the url of the user page

```sh
$ https://sauna-ikitai.com/saunners/<sauna-ikitai-id> 
```

sakatsu badge is generated from saunadge command.

```sh
$ pip install saunadge
$ saunadge -i <saunaikitai-id> -s flat-square
[![sakatsu badge](https://img.shields.io/endpoint.svg?url=https://saunadge-gjqqouyuca-an.a.run.app/api/v1/badge/46531&style=flat-square)](https://sauna-ikitai.com/saunners/46531)
```

## Badge

format for Markdown

```sh
[![sakatsu badge](https://img.shields.io/endpoint.svg?url=https://saunadge-gjqqouyuca-an.a.run.app/api/v1/badge/<saunai-kitai-id>&style=flat-square)](https://sauna-ikitai.com/saunners/<saunai-kitai-id>)
```

## TODO
- [ ] custom color
