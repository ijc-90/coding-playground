def contacts(queries):
    contactList = []
    #
    # Write your code here.
    #
    result = []
    for query in queries:
        if query[0] == 'add':
            contactList.append(query[1])
        if query[0] == 'find':
            def filterGenerator(valueToFilter):
                return lambda x : (x.find(query[1]) != -1)
            found = list(filter(lambda x: x.find(query[1]) != -1, contactList))
            result.append(len(found))
    return result


print(contacts([['add', 'eouecvksgllpvfxfvndu'], ['find', 'zivh'], ['add', 'uugxgcrtujxzyjysqrhu'], ['find', 'of'], ['add', 'ryhlozedmgzcmjdfjhte'], ['find', 'uqaqv'], ['add', 'ibfzenldsdltkjbbsccq'], ['find', 'bmcop'], ['add', 'vvxwlttswneoosvgfezt'], ['find', 've'], ['add', 'qimoqjtjypqupwwrueew'], ['find', 'ccyc'], ['add', 'nkaetboylnjbxxvhzupk'], ['find', 'lre'], ['add', 'rdzddgjryupsyhhbjtmx'], ['find', 'hhn'], ['add', 'kudnlccqbvkizsfdbwxy'], ['find', 'yyr'], ['add', 'jgahjespbkxxeqnzwpjr']]))