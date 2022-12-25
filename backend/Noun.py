def get_info_noun_ending_from_noun(ending):
   if ending in noun_noun_to_noun_more_used:
      return "n"
   elif ending in agent_noun:
      return "agnt"
   elif ending in noun_noun_to_noun_less_used:
      return "n"
   elif ending in noun_noun_to_noun_useless:
      return "n"
   else:
      return 'none'
def get_info_noun_ending_from_verb(ending):
   if ending in noun_verb_to_noun_more_used:
      return "n"
   elif ending in noun_verb_to_noun_less_used:
      return "n"
   elif ending in noun_verb_to_noun_useless:
      return "n"
   else:
      return 'none'
agent_noun = {
    'чы', 'чи', 'чу', 'чү'
}

noun_noun_to_noun_more_used = {
   'кана',
   "лык", "лик", "лук", "лүк",
   "тык", "тик", "тук", "түк",
   "дык", "дик", "дук", "дүк",
   "чылык", "чилик", "чулук", "чүлүк",
   "лаш", "леш", "лош", "лөш",
   "даш", "деш", "дош", "дөш",
   "таш", "теш", "тош", "төш",
}
noun_noun_to_noun_less_used = {
   "кер", "гер", 'көр',  #соодагер
   "кор", #ашкор
   "поз", 'боз',
   "стан",
   "ча", "че", "чо", "чө", #бакча
   "чык", "чик", "чук", "чүк",   #көлчүк
   'ак', 'ек', 'ок', 'өк',    #кезек
   'дырык', 'дурук', 'дүрүк', 'турук', 'түрүк', #ооздурук
   'кеч', #арабакеч
   'тай', #агатай
}
noun_noun_to_noun_useless = {
   'а', 'е',   #карта
   'ай', 'өй',     #көкөй
   'аке',   #тайаке
   'алак', 'олок', 'елек', #кызалак
   'ан', 'ен', 'он',   #эрен
   'аң', 'оң', 'ең', 'өң',   #жашаң
   'ас', 'ес', 'ос', 'өс',   #белес
   'ат', 'от', 'ет',   #канат
   'гай', 'кей', 'көй',   #карагай
   'гак', 'как', 'кок',   #капкак
   'гый',    #кудагый
   #'дан',    #чыгдан
   'ек',    #коёнек
   'жын', 'жин', 'жүн',    #кунажын
   'күр',    #түпкүр
   'күч',   #түпкүч
   'лак',    #тайлак
   'мар', 'мер', 'мөр',    #башмак
   'мач', 'меч',    #жармач
   'са', 'сө', 'се', 'со',   #дөңсө
   #'той',    #жолтой
   'так', 'тек',   #жеңилтек
   'чак', 'чек', 'чөк',    #келинчек
   'чар', 'чер', 'чор',    #букачар
   'чын',   #кулакчын
   'ык', 'ик', 'ук', 'үк',    #көчүк
   'үр',   #дүмүр


}
noun_verb_to_noun_more_used = {
   "ак", "ек", "ук", "үк", "ык", "ок", "ик", "өк", #калак
   'арман', 'ерман', 'өрман', 'ирмен', 'урман', #аларман
   'гы', 'кы', 'ки', 'ги', 'ку', 'кү', 'гу', 'гү', #ачыткы
   'гын', 'кын', 'гин', 'кин', 'гун', 'гүн', 'кун', 'күн', #качкын
   'гыч', 'гуч', 'гүч', 'гич', 'кыч', 'куч', 'күч', 'кич', #аткыч
   "ым", "им", "ум", "үм", 'ам', 'ом', 'өм', #агым
   "ма", "ме",'мо', 'мө', #басма
   "мак", "мек",'мок', 'мөк', #иймек
   'ын', 'ин', 'ун', 'үн', 'н', #агын
   "ынды", "инди", "унду", "үндү", 'енди', #кесинди
   'ооч', 'өөч',  #баяндооч
   "ыш", "иш", "уш", "үш", #алыш
   'ыч', 'ич', 'уч', 'үч', 'ч', #багыныч, урунч
   'ылдак', 'улдак', 'үлдөк', #арылдак
}
noun_verb_to_noun_less_used = {
   "аан", "оон", "өөн",  #жыгаан
   "гак", "гек", "гок", "гөк", "как", "кек", "кок", "көк", #баткак
   'ган', 'кан', 'гөн', 'көн',  #жараткан
   'ды', 'ты', 'ту', 'ду', 'тү', 'дү',  #бышты
   'ал', 'ыл', 'өл', 'ул', 'ол',  #курал
   "ылга", "илге", "алга", "улга", 'өлгө', 'олго',  #демилге
   "макей", "мекей",'мокей', 'мөкей', #алмакей
   "мал",'мол', 'мөл', #ташымал
   'мыш', 'муш', 'мүш', 'миш',  #кылмыш
   "ныч", "нүч", "нч",  #таяныч, суранч
   'оо', 'өө',  #жайлоо, суроо
   'ыт', 'ит', 'ут', 'үт', 'т', #жайыт
   "уу", "үү", #сүйүү
   'чак', 'чек', 'чок', 'чөк', #бөлчөк
}
noun_verb_to_noun_useless = {
   "а", "ө", "өөн",  #жара
   "ага", "ого", "еге", "өгө", #босого
   'ака',  #жарака
   'аке', 'еке',  #жалжаке
   'алак', 'елек', 'өлөк',   #жапалак
   "ан",  #жылан
   "анак", "өнөк", #көзөнөк
   "аса",'есе', 'өсө', #бересе
   'ат', 'өт',  #өлөт
   "ач", "өч",  #калач, көмөч
   'аша', 'еше', 'ошо'  #киреше
   'га', 'ка', 'ке', 'ге',  #тутка
   'галак', 'калак', 'голок',  #кайкалак
   'гылык', 'килик', 'гүлүк', #ичкилик
   'дак', 'так', 'дөк', #быштак
   'ды', 'ди', #каралды
   'дык', 'дик', 'тик', #калдык
   'й', #куркулдай
   'лжы',   #аралжы
   'ман', 'мөн', #көчмөн
   'мач', #жаңылмач
   'мжы', 'мжу',  #сурамжы
   'мта', #байламта
   'мча', #кошумча
   'нак', 'нөк', #жарнак
   'оок', #тырмоок
   'оол', 'өөл', #кароол
   'оон', 'өөн', #сүрөөн
   'пооч', #айланпооч
   'ты', #жарты
   'уур', 'үүр', #чукуур
   'ы', 'у', #соку
   'ымта', #барымта
   'ымча', 'умча', #алымча
   'ың', 'өң', 'оң', #козголоң

}