import requests
import soundfile
import os
import shutil
from playsound import playsound


def delete_files():
    # The path of the directory of audios
    directory_path = "./audios"
    # Get a list of all the files and directories in the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        # Check if the item is a file or directory
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)


def get_input():
    # prompt for input
    print("You:")
    user_input = input()
    return user_input


def get_token():
    # token = input("Copy your session token from ChatGPT and press Enter \n")
    token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..mjfFG-zkNbwviOPO.pj0iB8OO0O44hBppDFl3qSRV3d1VzTuY1Ff8cY1VilD-7F8cEkdXHcqbhzGz6lpYK-j1YmUoxShos6X5zAXC879L9llPV1mnWJPFChK-3X_1vp-_pJ4PJu223vkY23poTKIJiNe6tTzgOMNKtonmt7mLsfIKyZxr-mEsboGgt2TQd_LRB2exdgSYkZyF1G5hINtvA7zC4l1_JaE-gVkp7kf-fBsf1oDwId2ichw5tNB089o6yI9XhHMZD0XxlG9aFZwjhoSzO0wmmY1iOW71oXF5Shv5gCmLn2GDayu_LP-xA7_FB5v0NJ6ktw_I6dHNSMIdxVFelNHhSdOF-gEGDipkAtsbXpd9PrwewlEjzCWIPx5qj7yPhfb_X5pxx6W92j8uQAejPVTXcfUB-PEOeN-sQuzZzekoal51yq-IAu3zZWx5w27vbqGBb3QLTVjasRIm59WD901F4HUwFnw-GlOWHB3_OA4AphNBHKds02wyg-nLmtEbnUWmbwTL83efLN79-x8nH9ly3uz4JTHuxXJfzySlrEEFu1aJvt1Of7MEfEftEhylVz8GKuH9oWIEQ_ZzzForOjw17z0r_fPWaKoZu6nTGS0RcyKaibHHrcXCycHoSPUbw-GMfnNF2iXyfsNu2B0dm2ghU1Dtg5m7xtbT6DuiC-g11YG9A4hjo0TJkv_YyRu3qmie4VEjIzXaiTx7hPse7DhlEJw0vlx3bPVIZuyj7OAeUQrliN0q9zd3ciUUotSTI_PfYNrs7uUbGnAZJPbT56ys6fINSirl3XHm99shKE9UE6W2Au_blXDPoEla8gnUNSpZkkeeOvLNfBTLKwTutqhkal5FaJ38cbHrGDwADiLvrB550P542cMWVYcLDSUIKiBkpUFVbiq5OgWbG-x-jVRGxrLsJ7WuWCkmhSGe0wxkLZC7YDe3lO9H_3mp8M-roifTSPhzX4sjPT9Cfmiu8lSi0efi2TNMP6N2SwObLtgfr5SEjP-rrxqdjknXqlKfJ_AyV5KV7auGdTeZynR3NKE4sK9wS7V8Ou6s6SmZxvqEtDfdy7qw24AKaQvxbypH8U2eWb4civy3Scci1HggphuzRnJPwaiRVOHRU3xUFhBqebUTlXCEdt1bgmMxknBcsTQlQYXQ5X2gwivhXoUbu5Moe87n6175Yu7Sms6fs6fjoQ1GmUcRK8g7N40R8uYykMvHhTkfXW7zT1oFHmqAj2ILvVFG-GM_GMKiGd5WkDC3RxBI8WoH8pHzwTtAknS64MRFvoZqbQDMP1xZ9a8etWvAZiYmHsTZCjawfVxrLgVJoCB1uVEKn6uqfN8ieHW-ltHqxPvY7a7405GMVZlVEMT9K1BvMy2b7MkxcU3vgqdTV02w_mil7uot5afrrw-svGw1RyXoQqeA1aE3h5emTRp22etrXJVdPp67zB6IIy8s6yBe-JIVTxbiLmYEyaVV61fOar3W5HI9FafUW4Je83a7y0y4xr0sI4O9zNSS8mrGyn_nSU8ox4D-KPGHk6QGKScgBPlmVPvE-lq1_0Ffi8_X8xTOKIWkof3Jmvv7fqJsmaBIYGnhjHYwV5kTq4pTLisWK4uip6ptIm75njPDH22qlGLemhVVPF22hbYNoK_2EQom33_G3pjPgPdN039DikmUrr-wTlsoXVhUieQFP0IgRfmxWLlrqRyOhVRUky2ThyzzwIIwk_qCmwLYLfW_gjuok7Jgf46iwpqE5bwyxyLqA-kdXBQryC2_ugt9N5Umc-AjTQQ1WsJ8JF-JXKXg305TWQ9jFfwFPbwjnU88BMqF347QMZWRXviRtXjtIHGIGo4F6y5a3xOk6Oo6EbQR_nnw7NvVuj7v0hFzrZR5WoE-oBiwCVM6SlsPmGn2whzqLhSn_q4NkKuG8HRuQ-Y_71lbS8sQaaHMl2mhgmeGQh07BIULVWVeS83oTZ3PQbhOQiW1uY76zUd2XML8UQ6F24c5IChuM0rcTIkR7GgL5e7kQziPFJFC78P6hME-PEcFaz_WEHMIK3p7qq16XuoEk9jECZnCi9r3mHO0hV3vzXgexNp92sUNH8i9h_VesmM8GJgjyHNtO4Wt58KNbO9uRzryEOvCypd1MKJ-uGkia7yw_G33lxD8K5VPxcbbWJK5sZoLavcrLM737T1Vnum5qNCrfphp-Y7ZXk0R_k-ztPP003v1PXajel4UHd_3lcTwZppYYAFYSK8l08eLA0XMWYfHdumpAKtfT_fKcgQBMkl7V-a-AXeN29FXo0Un5A46ri2gnLyQ9EEei-uZzteqkDrgoTX7LxhUcKbzoqHhQ-dJLEplAosYipMjgZ_w51wOKd4QKyulup7qBM08GirA_2-11K9p9go-dsGU3UDUrzELagcMPfybx1jOdPgBWHeKF9rau_N-dv5ZfhnvExvt06-fQ_2njv8Iu26YyL2fxRJUUweS5WIgvfpFRhwzsVBKPqqDgOsUJ0se70lb5uHaNNBD6eYYRtd2I7j0BAhzi_0b6lK3I1loIrG4e00RutNNb_q3tL-MNlnSWGwNKoFiAIvlVIx3agOnFFHNaQMVZAQ-I78WeCaUJfk94LquIe6UPeJM5TO_dlkLmXaY-gSbBwXracZnq0IubhMbgy3Oi-cqw_zWGVnmshK_nuDt0eAZK12PCeC4AIu2wOvYrnEvEITbJYIzTb8.nGUOYyXDEifShoiDF6NegA"
    return token


def get_audio(answer):
    # MoeGoe Azure Cloud Function API endpoint
    URL = "https://moegoe.azurewebsites.net/api/speak"
    # The parameters for the API request
    params = {
        "text": answer,
        "id": 0,
    }
    # Send the API request
    response = requests.get(url=URL, params=params)
    # Get the binary data of the audio file
    audio_data = response.content
    # Save the audio file
    filename = "audios/output.wav"
    with open(filename, "wb") as f:
        f.write(audio_data)
    playsound(filename, True)  # Play the audio file
