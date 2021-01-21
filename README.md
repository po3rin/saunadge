# saunadge

saunadge lets you to generate sakatu(サ活/サウナ活動) badge. saunadge server aggregates from the data over [SAUNA-IKITAI](https://sauna-ikitai.com/).

## example

[![blog badge](https://img.shields.io/endpoint?url=https://saunadge-gjqqouyuca-an.a.run.app/api/v1/badge/46531&style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAYAAACOEfKtAAAABHNCSVQICAgIfAhkiAAABQxJREFUeJztnEtsFVUYx3+fRVCQR5ESfBDARzQGQ5CobUk00bJxKd3ploXpggWJceHGrTE+FobEGBN2LnwmxvhIIEBQIDWRlzEVX0QSCIlChdLG4t/FuY+h3vbee2bOnJkyv2SSc9NzvvPNv9935syZmQMVAEjqlbRd0m5JpztttyCkU0VG0kJgANhWO7YAPd3auaEElLQRGMIJ9gRwW1qb81pASWtoCrYNuCPrPuaVgJIWA0/ixBoCHg7dZ6kFlNQDPEIzwgaBhXn6UDoBJd1DM8KeAlbG9Mdidu6DJOXRj5l1pM1NoR2Z70RLYUkLgE24cWsA2Gpm62L5MxNJy4H1iWMDsK52rDWzPshRQEkrcUINAFuBR4ElefXvwcU5/napXggioCQDHqQp1kDtd+nG3FmYqBcyEVDSElxE1cUaIPLVMTBT9YKXgJLuwo1dgzjRNvvaKil/1wu+J/1HRo6Ulav1QqGjRtIiXHT346K9P65HDdKlcCgSQ0N/7dgCLIrqVGvG64VCCUh5hobJeqG6E/GjkcKVgH40JtKVgH5UKZySKoVTUqVwSqoITEljDGzMA2vPF6ajuFM+GhPpZASmfkZ6A9EyhRdHcKSsNBYTkgIW8Z6zqDSWs5ICLo3gSFlpmcK3RnCkrDSW9KsU9uNyvZAUcFkER8pKyxS+JYIjZeVKvVClsB8NAZMr0ssjOFIkzpvZmm4bVSnc5LhPoyqFm5zwaZQU8EZP4e99GlUR2OSYT6OyjIGT7auk4jJwyqdh8ipclIn0NPAdcKB2HDezM5LOAncG6nPUzK75NEwKGDOFfwa+Br4E9pnZpRZ1Qgp41LdhUsBoiwlmdl8n1QK6cNi3YZmWs9YHtP2Nb8NSXIUl3QusCmR+zMzO+zYuy5L+MwFtH0jTuCwPlZ4PaHtvmsaFT2FJm4DHQpkH9qUxkBSwqJ8cjAS0fdLMzqUxUGgBJa0ibPp+ldZAYx5oZje3q5zXd2oJdhJ2fvp5WgNdTU5DCdjqwz5Jy4DfgN4QfeJez1htZlNta85BkV8uGiGceABfpBUP4gr4L/AR7kOd65C0FNgVuP9PsjAS4y39SWAP8JqZzba9yE7g9oA+TJHB+Nc1SscFSa9IWt2mj15Jf6Xsqx0fZ6VJHhF4Gngd2GNmE+0qAy8BK8K6xPuB7bemy//yIUnPSup4nJV0t6SJzOPtesbldvfInw6cuybpQ0mDnvbfDSqd452sdenmBGfjqtyeU50sjM5m+yFJ/+Qg4ONZatLtSc6kowtDh7Y/zUE8r2e/mZFw5CdJLyijsUTSUA7iSdKOLPxNc6JdXxg6sNkj6UQO4l2QlPl9dVfTGDP7311DBuwANgawO5O3zexq+2rdEXUXDUkrgDGgL3BXF4ENZjbXViZexF5MeJnw4gG8EUI8iBiBku7HvREV+lHCOeABMxtvW9ODmBH4Kvk8h3kxlHjRkPR0DlddSdovt4tSMHJPYbnNX4/htoIKyTiw2cx+CdlJjBTeRXjxAEZCi5c7ktZLuhI4bY9K2p7XOeW9Iv0W2b9CImAU+Az4wMx+yNh+MZA0nGGU/S7pPUnPyW11HI1cLiJyD8hPAb6rNmeB/cBBYK+ZjWXlW1rySuHddC6egB+BQzjBDprZr6EcS0twASUNA8NzVPkT94bokdpxeJZXfAtJ0BSW1AecpBl907g54BFqohUpHX0ILeCbwFrgW5xooyGWlGLyH4KgDFtok8K+AAAAAElFTkSuQmCC)](https://sauna-ikitai.com/saunners/46531)

```sh
[![blog badge](https://img.shields.io/endpoint?url=https://saunadge-gjqqouyuca-an.a.run.app/api/v1/badge/46531&style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAYAAACOEfKtAAAABHNCSVQICAgIfAhkiAAABQxJREFUeJztnEtsFVUYx3+fRVCQR5ESfBDARzQGQ5CobUk00bJxKd3ploXpggWJceHGrTE+FobEGBN2LnwmxvhIIEBQIDWRlzEVX0QSCIlChdLG4t/FuY+h3vbee2bOnJkyv2SSc9NzvvPNv9935syZmQMVAEjqlbRd0m5JpztttyCkU0VG0kJgANhWO7YAPd3auaEElLQRGMIJ9gRwW1qb81pASWtoCrYNuCPrPuaVgJIWA0/ixBoCHg7dZ6kFlNQDPEIzwgaBhXn6UDoBJd1DM8KeAlbG9Mdidu6DJOXRj5l1pM1NoR2Z70RLYUkLgE24cWsA2Gpm62L5MxNJy4H1iWMDsK52rDWzPshRQEkrcUINAFuBR4ElefXvwcU5/napXggioCQDHqQp1kDtd+nG3FmYqBcyEVDSElxE1cUaIPLVMTBT9YKXgJLuwo1dgzjRNvvaKil/1wu+J/1HRo6Ulav1QqGjRtIiXHT346K9P65HDdKlcCgSQ0N/7dgCLIrqVGvG64VCCUh5hobJeqG6E/GjkcKVgH40JtKVgH5UKZySKoVTUqVwSqoITEljDGzMA2vPF6ajuFM+GhPpZASmfkZ6A9EyhRdHcKSsNBYTkgIW8Z6zqDSWs5ICLo3gSFlpmcK3RnCkrDSW9KsU9uNyvZAUcFkER8pKyxS+JYIjZeVKvVClsB8NAZMr0ssjOFIkzpvZmm4bVSnc5LhPoyqFm5zwaZQU8EZP4e99GlUR2OSYT6OyjIGT7auk4jJwyqdh8ipclIn0NPAdcKB2HDezM5LOAncG6nPUzK75NEwKGDOFfwa+Br4E9pnZpRZ1Qgp41LdhUsBoiwlmdl8n1QK6cNi3YZmWs9YHtP2Nb8NSXIUl3QusCmR+zMzO+zYuy5L+MwFtH0jTuCwPlZ4PaHtvmsaFT2FJm4DHQpkH9qUxkBSwqJ8cjAS0fdLMzqUxUGgBJa0ibPp+ldZAYx5oZje3q5zXd2oJdhJ2fvp5WgNdTU5DCdjqwz5Jy4DfgN4QfeJez1htZlNta85BkV8uGiGceABfpBUP4gr4L/AR7kOd65C0FNgVuP9PsjAS4y39SWAP8JqZzba9yE7g9oA+TJHB+Nc1SscFSa9IWt2mj15Jf6Xsqx0fZ6VJHhF4Gngd2GNmE+0qAy8BK8K6xPuB7bemy//yIUnPSup4nJV0t6SJzOPtesbldvfInw6cuybpQ0mDnvbfDSqd452sdenmBGfjqtyeU50sjM5m+yFJ/+Qg4ONZatLtSc6kowtDh7Y/zUE8r2e/mZFw5CdJLyijsUTSUA7iSdKOLPxNc6JdXxg6sNkj6UQO4l2QlPl9dVfTGDP7311DBuwANgawO5O3zexq+2rdEXUXDUkrgDGgL3BXF4ENZjbXViZexF5MeJnw4gG8EUI8iBiBku7HvREV+lHCOeABMxtvW9ODmBH4Kvk8h3kxlHjRkPR0DlddSdovt4tSMHJPYbnNX4/htoIKyTiw2cx+CdlJjBTeRXjxAEZCi5c7ktZLuhI4bY9K2p7XOeW9Iv0W2b9CImAU+Az4wMx+yNh+MZA0nGGU/S7pPUnPyW11HI1cLiJyD8hPAb6rNmeB/cBBYK+ZjWXlW1rySuHddC6egB+BQzjBDprZr6EcS0twASUNA8NzVPkT94bokdpxeJZXfAtJ0BSW1AecpBl907g54BFqohUpHX0ILeCbwFrgW5xooyGWlGLyH4KgDFtok8K+AAAAAElFTkSuQmCC)](https://sauna-ikitai.com/saunners/46531)
```

