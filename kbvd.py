import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

data_penumpang = pd.read_csv('jumlah-penumpang-pso-ker.csv', sep=';')
data_pelayanan = pd.read_csv('tingkat-pelayanan.csv', sep=';')
data_produksi = pd.read_csv('produksi-penumpang-dan-b.csv', sep=';')
data_kelompok_barang = pd.read_csv('produksi-barang-kelompok.csv', sep=';')

#NUMERIK
data_pelayanan['PNP BER TEPAT (%)'] = pd.to_numeric(data_pelayanan['PNP BER TEPAT (%)'].str.replace(',', '.'))
data_pelayanan['PNP DTG TEPAT (%)'] = pd.to_numeric(data_pelayanan['PNP DTG TEPAT (%)'].str.replace(',', '.'))
data_pelayanan['BRG BER TEPAT (%)'] = pd.to_numeric(data_pelayanan['BRG BER TEPAT (%)'].str.replace(',', '.'))
data_pelayanan['BRG DTG TEPAT (%)'] = pd.to_numeric(data_pelayanan['BRG DTG TEPAT (%)'].str.replace(',', '.'))

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Dashboard Transportasi Umum"),

    # Dropdown untuk memilih kategori kereta api
    dcc.Dropdown(
        id='category-dropdown',
        options=[
            {'label': 'Ekonomi Jarak Jauh', 'value': 'Jumlah Penumpang PSO Kereta Api Ekonomi Jarak Jauh'},
            {'label': 'Ekonomi Jarak Sedang', 'value': 'Jumlah Penumpang PSO Kereta Api Ekonomi Jarak Sedang'},
            {'label': 'Ekonomi Jarak Dekat', 'value': 'Jumlah Penumpang PSO Kereta Api Ekonomi Jarak Dekat'}
        ],
        value='Jumlah Penumpang PSO Kereta Api Ekonomi Jarak Jauh',
        clearable=False
    ),

    dcc.Graph(id='passenger-trend'),

    # dcc.Graph(
    #     id='passenger-by-station',
    #     figure={
    #         'data': [
    #             go.Bar(
    #                 x=data_penumpang_by_station['Stasiun'],
    #                 y=data_penumpang_by_station['Jumlah Penumpang'],
    #                 name='Jumlah Penumpang per Stasiun'
    #             )
    #         ],
    #         'layout': go.Layout(
    #             title='Perbandingan Jumlah Penumpang Antar Stasiun',
    #             xaxis={'title': 'Stasiun'},
    #             yaxis={'title': 'Jumlah Penumpang'},
    #             barmode='group'
    #         )
    #     }
    # ),

    # dcc.Graph(
    #     id='passenger-by-city',
    #     figure={
    #         'data': [
    #             go.Bar(
    #                 x=data_penumpang_by_city['Kota'],
    #                 y=data_penumpang_by_city['Jumlah Penumpang'],
    #                 name='Jumlah Penumpang per Kota'
    #             )
    #         ],
    #         'layout': go.Layout(
    #             title='Perbandingan Jumlah Penumpang Antar Kota',
    #             xaxis={'title': 'Kota'},
    #             yaxis={'title': 'Jumlah Penumpang'},
    #             barmode='group'
    #         )
    #     }
    # ),

    dcc.Graph(
        id='service-timeliness',
        figure={
            'data': [
                go.Bar(
                    x=data_pelayanan['Category'],
                    y=data_pelayanan['PNP BER TEPAT (%)'],
                    name='Berangkat Tepat Waktu'
                ),
                go.Bar(
                    x=data_pelayanan['Category'],
                    y=data_pelayanan['PNP DTG TEPAT (%)'],
                    name='Datang Tepat Waktu'
                )
            ],
            'layout': go.Layout(
                title='Tingkat Ketepatan Waktu Kereta Api',
                xaxis={'title': 'Bulan'},
                yaxis={'title': 'Persentase (%)'},
                barmode='group'
            )
        }
    ),

    dcc.Graph(
        id='production-comparison',
        figure={
            'data': [
                go.Bar(
                    x=data_produksi['Category'],
                    y=data_produksi['Penumpang (Jawa)'],
                    name='Penumpang (Jawa)'
                ),
                go.Bar(
                    x=data_produksi['Category'],
                    y=data_produksi['Barang (Jawa)'],
                    name='Barang (Jawa)'
                ),
                go.Bar(
                    x=data_produksi['Category'],
                    y=data_produksi['Penumpang (Sumatera)'],
                    name='Penumpang (Sumatera)'
                ),
                go.Bar(
                    x=data_produksi['Category'],
                    y=data_produksi['Barang (Sumatera)'],
                    name='Barang (Sumatera)'
                )
            ],
            'layout': go.Layout(
                title='Produksi Penumpang dan Barang di Jawa dan Sumatera',
                xaxis={'title': 'Bulan'},
                yaxis={'title': 'Jumlah'},
                barmode='group'
            )
        }
    ),

    dcc.Graph(
        id='goods-production',
        figure={
            'data': [
                go.Bar(
                    x=data_kelompok_barang['Category'],
                    y=data_kelompok_barang[' Minyak Bumi (BBM)'],
                    name='Minyak Bumi (BBM)'
                ),
                go.Bar(
                    x=data_kelompok_barang['Category'],
                    y=data_kelompok_barang['P u p u k'],
                    name='Pupuk'
                ),
                go.Bar(
                    x=data_kelompok_barang['Category'],
                    y=data_kelompok_barang['S e m e n'],
                    name='Semen'
                ),
                go.Bar(
                    x=data_kelompok_barang['Category'],
                    y=data_kelompok_barang['Batubara'],
                    name='Batubara'
                ),
                go.Bar(
                    x=data_kelompok_barang['Category'],
                    y=data_kelompok_barang['Hasil Perkebunan'],
                    name='Hasil Perkebunan'
                ),
                go.Bar(
                    x=data_kelompok_barang['Category'],
                    y=data_kelompok_barang['Peti Kemas'],
                    name='Peti Kemas'
                ),
                go.Bar(
                    x=data_kelompok_barang['Category'],
                    y=data_kelompok_barang['Pasir Kuarsa'],
                    name='Pasir Kuarsa'
                ),
                go.Bar(
                    x=data_kelompok_barang['Category'],
                    y=data_kelompok_barang['Karet&Klinker'],
                    name='Karet & Klinker'
                ),
                go.Bar(
                    x=data_kelompok_barang['Category'],
                    y=data_kelompok_barang['B. H. P.(Barang Hantaran Penumpang)'],
                    name='Barang Hantaran Penumpang (B.H.P.)'
                ),
                go.Bar(
                    x=data_kelompok_barang['Category'],
                    y=data_kelompok_barang['Lain-Lain'],
                    name='Lain-Lain'
                )
            ],
            'layout': go.Layout(
                title='Produksi Barang Kelompok per Bulan',
                xaxis={'title': 'Bulan'},
                yaxis={'title': 'Jumlah'},
                barmode='group'
            )
        }
    ),

    html.Div([
        html.H3("Narasi Data"),
        html.P("Dashboard ini menyajikan informasi penting mengenai transportasi umum di Indonesia."),
        html.P("Grafik pertama menunjukkan jumlah penumpang kereta api ekonomi untuk berbagai kategori jarak (Jauh, Sedang, Dekat) dari bulan ke bulan. "
                "Terlihat bahwa jumlah penumpang mengalami peningkatan signifikan pada bulan Mei, yang kemungkinan besar terkait dengan liburan Lebaran."),
        # html.P("Grafik kedua menggambarkan tingkat ketepatan waktu kereta api, baik untuk keberangkatan maupun kedatangan. "
        #         "Bulan Juli menunjukkan tingkat ketepatan waktu tertinggi, yang mengindikasikan peningkatan kualitas layanan."),
        # html.P("Grafik ketiga membandingkan produksi penumpang dan barang yang diangkut di Jawa dan Sumatera. "
        #         "Jawa memiliki volume penumpang yang jauh lebih tinggi dibandingkan Sumatera, menunjukkan potensi untuk meningkatkan layanan di wilayah Sumatera."),
        html.P("Grafik keempat menunjukkan perbandingan jumlah penumpang antar stasiun. "
                "Data ini memberikan wawasan tentang stasiun mana yang paling banyak digunakan oleh penumpang."),
        html.P("Grafik kelima menunjukkan perbandingan jumlah penumpang antar kota. "
                "Kota-kota dengan jumlah penumpang tertinggi dapat menjadi fokus untuk pengembangan infrastruktur transportasi."),
        html.P("Grafik keenam menunjukkan produksi barang kelompok per bulan. "
                "Batubara dan Minyak Bumi (BBM) merupakan barang dengan produksi tertinggi, sementara Pasir Kuarsa dan Karet & Klinker menunjukkan produksi yang lebih rendah. "
                "Data ini memberikan wawasan tentang tren produksi barang di Indonesia dan dapat membantu dalam perencanaan dan pengambilan keputusan.")
    ])
])

@app.callback(
    Output('passenger-trend', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_graph(selected_category):
    figure = {
        'data': [
            go.Scatter(
                x=data_penumpang['Category'],
                y=data_penumpang[selected_category],
                mode='lines+markers',
                name=selected_category
            )
        ],
        'layout': go.Layout(
            title=f'Jumlah Penumpang Kereta Api ({selected_category})',
            xaxis={'title': 'Bulan'},
            yaxis={'title': 'Jumlah Penumpang'},
            hovermode='closest'
        )
    }
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
