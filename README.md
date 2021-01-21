# saunadge

![Build image](https://github.com/po3rin/saunadge/workflows/Build%20image/badge.svg)

saunadge lets you to generate sakatu(サ活/サウナ活動) badge. saunadge server aggregates from the data over [SAUNA-IKITAI](https://sauna-ikitai.com/).

## Usage

```sh
$ pip install saunadge
$ saunadge -i <saunaikitai-id>
[![sakatsu badge](https://img.shields.io/endpoint.svg?url=https://saunadge-gjqqouyuca-an.a.run.app/api/v1/badge/46531&style=flat-square)](https://sauna-ikitai.com/saunners/46531)
```

[![sakatsu badge](https://img.shields.io/endpoint.svg?url=https://saunadge-gjqqouyuca-an.a.run.app/api/v1/badge/46531&style=flat-square)](https://sauna-ikitai.com/saunners/46531)

## Badge

format for Markdown

```sh
[![sakatsu badge](https://img.shields.io/endpoint.svg?url=https://saunadge-gjqqouyuca-an.a.run.app/api/v1/badge/<saunai-kitai-id>&style=flat-square)](https://sauna-ikitai.com/saunners/<saunai-kitai-id>)
```
