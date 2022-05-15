# Abilities of my bot

comamnds:
/start - starting bot, send a greeting message
/get_parsed_crypto - send all avalilable names of crypto in db already
/get_crypto - send info about choosen (entered) crypto
/get_exchange_rate - send info about now exchange rate entered crypto
/info - send message about all methods (inline), you can choose interested method and look, how it works
/goodbye - send massage with random goodbye to user

menus:
    start:
        button1 - show available databases (bot sending names of crypto, which already parsed)
        button2 - get available database (bot sending file in csv format)
        button3 - create crypto db (bot start parsing and saving data in db, send file with parsed crypto in csv format)
        button4 - get random db
    get parsed crypto:
        4 buttons of available crypto db + 2 buttons (prev and next page of bases)
    info:
        4 buttons of available methods + 2 buttons (prev and next page of methods)