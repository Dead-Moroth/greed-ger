# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# Part of the translation by https://github.com/DarrenWestwood

# Currency symbol
currency_symbol = "€"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} verfügbar"

# Copies of a product in cart
in_cart_format_string = "{quantity} im Einkaufswagen"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Bestellung #{id}"

# Order info string, shown to the admins
order_format_string = "von {user}\n" \
                      "Erstellt am {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "SUMME: <b>{value}</b>\n" \
                      "\n" \
                      "Notiz: {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Bestellung {status_text}</b>\n" \
                           "{items}\n" \
                           "SUMME: <b>{value}</b>\n" \
                           "\n" \
                           "Notiz: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>Transaktionen werden geladen...\n" \
                       "Bitte warten.</i>"

# Transactions page
transactions_page = "Seite <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "Eine 📄 CSV-Datei mit allen in der Bot-Datenbank gespeicherten Transaktionen wurde generiert.\n" \
              "Du kannst diese Datei mit Programmen wie LibreOffice Calc öffnen, um sie zu berarbeiten"

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Hallo!\n" \
                           "Willkommen bei greed!\n" \
                           "Dies ist eine 🅱️ <b>Beta</b> Version dieser Software.\n" \
                           "Diese ist zwar voll einsatzbereit, jedoch kann es zu Fehlern kommen.\n" \
                           "Solltest du welche finden, teile diese bitte unter https://github.com/Steffo99/greed/issues mit."

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "Was möchtest du tun?\n" \
                              "💰 Du hast <b>{credit}</b> auf deinem Guthabenkonto.\n" \
                              "\n" \
                              "<i>Wähle unten eine Aktion um zu beginnen.\n" \
                              " Solltest du keine Aktionen sehen können, kannst du diese Anzeigen lassen, indem du unten" \ 
                              " auf die 4 kleine Quadrate drückst.</i>"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "Du bist der 💼 <b>Manager</b> dieses Stores!\n" \
                               "Was möchtest du tun?\n" \
                               "\n" \
                               "<i>Wähle unten eine Aktion um zu beginnen.\n" \
                              " Solltest du keine Aktionen sehen können, kannst du diese Anzeigen lassen, indem du unten" \ 
                              " auf die 4 kleine Quadrate drückst.</i>"

# Conversation: select a payment method
conversation_payment_method = "Wie möchtest du Guthaben aufladen?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ Welchen Artikel möchtest du bearbeiten?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ Welcher Artikel soll gelöscht werden?"

# Conversation: select a user to edit
conversation_admin_select_user = "Wähle einen Benutzer zur Bearbeitung aus."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Füge Produkte hinzu, indem du auf den Hinzufügen Knopf unter den Artikeln drückst." \
                            " Kehre zu dieser Nachricht zurück und bestätige mit Fertig," \
                            " wenn du mit der Bestellung fertig bist.</i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 In deinem Warenkorb liegen folgende Produkte:\n" \
                            "{product_list}" \
                            "Summe: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>Um fortzufahren, bestätige mit Fertig.\n" \
                            "Um abzubrechen wähle Abbrechen.</i>"

# Live orders mode: start
conversation_live_orders_start = "Du bist im <b>Live</b> Bestellungsmodus\n" \
                                 "Alle neuen Bestellungen werden hier angezeigt. Du kannst" \
                                 " hier diese als ✅ komplett" \
                                 " oder als ✴️ erstattet markieren."

# Live orders mode: stop receiving messages
conversation_live_orders_stop = "<i>Wähle Stop, um den Live-Modus zu stoppen</i>"

# Conversation: help menu has been opened
conversation_open_help_menu = "Wie können wir helfen?"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = "Bist du sicher, dass du diesen Benutzer als 💼 Manager wählen möchtest?\n" \
                                       "Diese Aktion lässt sich <b>nicht</b> rückgängig machen!"

# Conversation: language select menu header
conversation_language_select = "Wähle eine Sprache:"

# Conversation: switching to user mode
conversation_switch_to_user_mode = " Du wechselst in den 👤 Kunden-Modus.\n" \
                                   "Um wieder in den 💼 Manager-Modus zu gelangen, tippe /start in das Nachrichtenfenster."

# Notification: the conversation has expired
conversation_expired = "🕐  Es wurde länger keine Aktion durchgeführt. Um Ressourcen zu sparen" \
                       " wurde die Session beendet.\n" \
                       "Um erneut zu starten, wähle das Kommando /start ."

# User menu: order
menu_order = "🛒 Bestellen"

# User menu: order status
menu_order_status = "🛍 Meine Bestellungen"

# User menu: add credit
menu_add_credit = "💵 Guthaben aufladen"

# User menu: bot info
menu_bot_info = "ℹ️ Bot Info"

# User menu: cash
menu_cash = "💵 Barzahlung"

# User menu: credit card
menu_credit_card = "💳 Kreditkartenzahlung"

# Admin menu: products
menu_products = "📝️ Produkte"

# Admin menu: orders
menu_orders = "📦 Bestellungen"

# Menu: transactions
menu_transactions = "💳 Transaktionsliste"

# Menu: edit credit
menu_edit_credit = "💰 Transaktion erzeugen"

# Admin menu: go to user mode
menu_user_mode = "👤 Zum Kunden-Modus wechseln"

# Admin menu: add product
menu_add_product = "✨ Neuer Artikel"

# Admin menu: delete product
menu_delete_product = "❌ PArtikel löschen"

# Menu: cancel
menu_cancel = "🔙 Abbrechen"

# Menu: skip
menu_skip = "⏭ Weiter"

# Menu: done
menu_done = "✅️ Fertig"

# Menu: pay invoice
menu_pay = "💳 Bezahlen"

# Menu: complete
menu_complete = "✅ Komplett"

# Menu: refund
menu_refund = "✴️ Erstatten"

# Menu: stop
menu_stop = "🛑 Stopp"

# Menu: add to cart
menu_add_to_cart = "➕ Hinzufügen"

# Menu: remove from cart
menu_remove_from_cart = "➖ Entfernen"

# Menu: help menu
menu_help = "❓ Hilfe / Support"

# Menu: guide
menu_guide = "📖 Anleitung"

# Menu: next page
menu_next = "▶️ Nächste"

# Menu: previous page
menu_previous = "◀️ Zurück"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Händler kontaktieren"

# Menu: generate transactions .csv file
menu_csv = "📄 .csv"

# Menu: edit admins list
menu_edit_admins = "🏵 Manager bearbeiten"

# Menu: language
menu_language = "🇩🇪 Sprache"

# Emoji: unprocessed order
emoji_not_processed = "*️⃣"

# Emoji: completed order
emoji_completed = "✅"

# Emoji: refunded order
emoji_refunded = "✴️"

# Emoji: yes
emoji_yes = "✅"

# Emoji: no
emoji_no = "🚫"

# Text: unprocessed order
text_not_processed = "ausstehend"

# Text: completed order
text_completed = "komplett"

# Text: refunded order
text_refunded = "erstattet"

# Add product: name?
ask_product_name = "Wie soll der Artikel heißen?"

# Add product: description?
ask_product_description = "Wie lautet die Beschreibung?"

# Add product: price?
ask_product_price = "Wie teuer soll der Artikel sein?\n" \
                    "Sende ein <code>X</code> wenn der Artikel nicht verkäuflich sein soll."

# Add product: image?
ask_product_image = "🖼 Wähle ein Produktbild aus.\n" \
                    "\n" \
                    "<i>Sende ein Foto oder überspringe diesen Schritt.</i>"

# Order product: notes?
ask_order_notes = "Möchtest du eine Bestellnotiz hinzufügen?\n" \
                  "💼 Diese ist für den Händler sichtbar.\n" \
                  "\n" \
                  "<i>Sende eine Nachricht mit der Notiz oder überspringe diesen Schritt.</i>"

# Refund product: reason?
ask_refund_reason = " Reklamationsgrung hinzufügen.\n" \
                    "👤  Sichtbar für den Kunden."

# Edit credit: notes?
ask_transaction_notes = " Füge dieser Transaktion eine Notiz hinzu.\n" \
                        "👤 Diese ist für den Kunden nach der Gutschrift oder Abbuchung sichtbar." \
                        " 💼 Admins sehen diese in der Transaktionsdatei."

# Edit credit: amount?
ask_credit = "Wie möchtest du das Kundenguthaben verändern?\n" \
             "\n" \
             "<i>Sende eine nachricht mit dem gewünschten Wert.\n" \
             "Nutze ein </i><code>+</code><i> um Guthaben dazu zu buchen" \
             " oder ein </i><code>-</code><i> um dieses zu entfernen.</i>"

# Header for the edit admin message
admin_properties = "<b>Rechte von {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "Artikel bearbeiten"

# Edit admin: can receive orders?
prop_receive_orders = "Bestellungen empfangen"

# Edit admin: can create transactions?
prop_create_transactions = "Transaktionen verwalten"

# Edit admin: show on help message?
prop_display_on_help = "den Kunden anzeigen"

# Thread has started downloading an image and might be unresponsive
downloading_image = "Foto wird hochgeladen!\n" \
                    "Dieser Prozess könnte etwas dauern... Bitte warten!\n" \
                    "Während des Uploads werden keine Kommandos verarbeitet."

# Edit product: current value
edit_current_value = "Aktuelles Guthaben:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Drücke Weiter um den Guthabenwert beizubehalten.</i>"

# Payment: cash payment info
payment_cash = "Barzahlung ist vor Ort möglich.\n" \
               "Teile uns nach einer Kreditkartenzahlung folgende ID mit:\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "Wieviel Kundenguthaben möchtest du aufladen?\n" \
                    "\n" \
                    "<i>Wähle einen Wert auf der Tastatur oder sende diesen manuell über das Chatfenster.</i>"

# Payment: add funds invoice title
payment_invoice_title = "Guthaben wird gebucht"

# Payment: add funds invoice description
payment_invoice_description = "Nach der Bezahlung werden {amount} Punkte gebucht."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "Aktualisieren"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Transaktionsgebühr"

# Notification: order has been placed
notification_order_placed = "Neuse Bestellung eingegangen:\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Deine Bestellung ist komplett!\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "Deine Bestellung wurde erstattet!\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️  Eine neue Transaktion wurde auf dein Konto gebucht:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Erstattungsgrund:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = 'Dieser Bot nutzt <a href="https://github.com/Steffo99/greed">greed</a>,' \
           ' ein Framework von @Steffo für Telegram Zahlungen. Veröffentlicht unter der' \
           ' <a href="https://github.com/Steffo99/greed/blob/master/LICENSE.txt">' \
           'Affero General Public Lizenz 3.0</a>.\n'

# Help: guide
help_msg = "greed's Anleitung ist verfügbar unter (Italienisch):\n" \
           "https://docs.google.com/document/d/1f4MKVr0B7RSQfWTSa_6ZO0LM4nPpky_GX_qdls3EHtQ/"

# Help: contact shopkeeper
contact_shopkeeper = "Derzeit besteht das Personal, das für die Benutzerunterstützung zur Verfügung steht, aus:\n" \
                     "{shopkeepers}\n" \
                     "<i>Drücke auf den gewünschten Namen um einen Mitarbeiter über Telegram zu kontaktieren</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ Der Artikel wurde erfolgreich hinzugefügt/bearbeitet!"

# Success: product has been added/edited to the database
success_product_deleted = "✅ Der Artikel wurde erfolgreich gelöscht!"

# Success: order has been created
success_order_created = "✅ Die Bestellung wurde erfolgreich versendet!\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ Die Bestellung #{order_id} wurde als Komplett markiert."

# Success: order was refunded successfully
success_order_refunded = "✴️ Bestellung #{order_id} wurde erstattet."

# Success: transaction was created successfully
success_transaction_created = "✅ Transaktion erfolgreich durchgeführt!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ Dieser Bot funktioniert nur in privaten Chats."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ Verbindung zum Bot wurde unterbrochen.\n" \
                           "Um erneut zu starten drücke auf /start"

# Error: a message was sent in a chat, but the worker for that chat is not ready.
error_worker_not_ready = "🕒 Verbindung zum Bot wird aufgebaut.\n" \
                         "Bitte warte ein wenig, bevor du weitere Kommandos sendest!"

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ Maximalbetrag pro Transaktion beträgt: {max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ Minimalbetrag pro Transaktion beträgt: {min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ Die Rechnung ist abgelaufen und wurde storniert. Um das Guthaben zu buchen, wähle die" \
                        " Guthaben hinzufügen Option."

# Error: a product with that name already exists
error_duplicate_name = "️⚠️ Ein Artikel mit diesem Namen existiert bereits."

# Error: not enough credit to order
error_not_enough_credit = "⚠️ Kundenguthaben reicht nicht aus, um eine Bestellung zu tätigen."

# Error: order has already been cleared
error_order_already_cleared = "⚠️  Diese Bestellung wurde bereits bearbeitet."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  Bisher wurden keine Bestellungen getätigt."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  Der gewählte Benutzer existiert nicht."

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Oh nein! Ein <b>Fehler</b> unterbrach die Verbindung.\n" \
                               "Der Fehler wurde uns mitgeteilt, damit wie diesen beheben können.\n" \
                               "Um erneut zu starten, drücke erneut auf /start "
