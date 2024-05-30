'''
Este projeto foi feito assistindo ao video do canal 'Programador Aventureiro'. link do video: https://youtu.be/kGNp24U5Oyo?si=HTjLxBWkTTALDZdU
'''

import flet as ft


def main(page: ft.Page):  # onde está todo o app criado
    page.bgcolor = ft.colors.BLACK  # o bgcolor autera a cor do fundo do app
    page.scroll = ft.ScrollMode.AUTO

    def change_main_image(e):  # trocando imagem, primaria pela segundaria
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
                main_image.src = elem.image_src
            else:
                elem.opacity = 0.5
        main_image.update()
        options.update()

    product_images = ft. Container(  # parte esquerda, imagan do produto
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=11/15,  # altura a largura do compomente

        content=ft.Column(  # ciando uma coluna
            # espaçamento entre a imagem principal e segundaria
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

            controls=[  # é uma lista de controle, controla os compomentes adicionado

                main_image := ft.Image(  # add uma imagem
                    src='https://images.tcdn.com.br/img/img_prod/475075/poltrona_opala_suede_pes_palito_d_rossi_36637_1_20201213195034.jpg',  # o caminho da imagem
                ),

                # proximo elemento depois da imagem
                options := ft.Row(

                    alignment=ft.MainAxisAlignment.CENTER,  # centraliza
                    controls=[

                        ft.Container(  # criando um container
                            image_src='https://images.tcdn.com.br/img/img_prod/475075/poltrona_opala_suede_pes_palito_d_rossi_36637_1_20201213195034.jpg',
                            width=80,  # altura da imagem
                            height=80,  # largura da imagem
                            opacity=1,  # opacidade
                            on_click=change_main_image  # quando clicar ativa a função 'change_main_image'
                        ),

                        ft.Container(  # criando um container
                            image_src='https://images-americanas.b2w.io/produtos/2561670282/imagens/poltrona-decorativa-opala-suede-capuccino-smf-decor/2561670282_1_large.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),

                        ft.Container(  # criando um container
                            image_src='https://images.tcdn.com.br/img/img_prod/706127/poltrona_decorativa_opala_suede_bordo_dora_bela_213_1_20191226154735.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        )

                    ]
                )
            ]
        )
    )

    product_details = ft.Container(  # parte direita, datalhes do produto
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=11/15,
        content=ft.Column(  # criando o conteudo
            controls=[
                ft.Text(
                    value='Poltrona',
                    color=ft.colors.AMBER,
                    height=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    value='Poltrona Moderna',
                    color=ft.colors.WHITE,
                    height=ft.FontWeight.BOLD,
                    size=30,

                ),
                
                ft.Text(value='Sala de estar', color=ft.colors.GREY, italic=True),

                ft.ResponsiveRow(
                    columns=12,
                    vertical_alignment= ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm': 6},
                            value='R$300,00',
                            color=ft.colors.WHITE,
                            size=30
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm': 6},
                            spacing=5,
                            wrap=False,
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.YELLOW if _ < 4 else ft.colors.WHITE,
                                ) for _ in range(5)
                            ]
                        )
                    ]
                ),
                ft.Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.WHITE,
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                    padding=ft.padding.all(10),
                                    content=ft.Text(
                                        value='uma poutrona cor amarela.',
                                        color=ft.colors.WHITE
                                    )
                            ),
                            
                        ),
                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='tem um metro.',
                                    color=ft.colors.WHITE
                                )
                            ),
                        )
                    ]
                ),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6,
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLACK,
                            label='Cor',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='Amarelo'),
                                ft.dropdown.Option(text='Cinza'),
                                ft.dropdown.Option(text='Vermelho'),
                            ]
                        ),
                        ft.Dropdown(
                            col=6,
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLACK,
                            label='Quantidade',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text=f'{num} unidade') for num in range(1, 11)
                            ]
                        ),
                    ]
                ),

                ft.Container(expand=True),

                ft.ElevatedButton(
                    width=900,
                    text='Adicionar a lista de desejos',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                            },
                        bgcolor={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                            ft.MaterialState.HOVERED: ft.colors.WHITE
                            },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                            ft.MaterialState.HOVERED: ft.colors.BLACK
                            },
                    )
                ),
                ft.ElevatedButton(
                    width=900,
                    text='Adicionar ao carrinho',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.AMBER)
                            },
                        bgcolor={
                            ft.MaterialState.DEFAULT: ft.colors.AMBER,
                            },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                            },
                    )
                )
            ]
        )


    )

    # este é o layout, o Container, pode ter varias propriedades, margem, cor, sombra, é onde é feito o front-end
    layout = ft.Container(
        width=900,  # está pasando o tamanho do container
        # height=200,#permite ver o Container
        # o minino de distancia do container para a borda da tela
        margin=ft.margin.all(30),
        # cria uma sombra em volta do container
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        # passa um linha reponsiva
        content=ft.ResponsiveRow(
            columns=12,  # quantas colunas tem a linha
            spacing=0,  # o espeços entre os compomentes
            run_spacing=0,  # o espeços entre os compomentes, mas quando um está encima do outro
            controls=[  # é uma lista de controle, controla os compomentes adicionado
                product_images,
                product_details
            ]
        )
    )

    page.add(layout)  # add o layout na aplicação
    # page.update()#atualiza a tela de aplicação


if __name__ == '__main__':
    # gera a tela de aplicação, e 'target=' mostra onde estão os detalhes da aplicação(no caso a função main)
    ft.app(target=main)
