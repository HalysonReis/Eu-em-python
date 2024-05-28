import flet as ft
import time


def main(page: ft.Page):  # onde está todo o app criado
    page.bgcolor = ft.colors.BLACK  # o bgcolor autera a cor do fundo do app

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
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,  # altura a largura do compomente

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

        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/16,
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
                ),
                
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
                # product_images,
                product_details
            ]
        )
    )

    page.add(layout)  # add o layout na aplicação
    # page.update()#atualiza a tela de aplicação


if __name__ == '__main__':
    # gera a tela de aplicação, e 'target=' mostra onde estão os detalhes da aplicação(no caso a função main)
    ft.app(target=main)
