def find_item_index(items_list, item):
  """Ищет первый индекс указанного элемента в списке.

  Args:
    items_list: Список элементов для поиска.
    item: Элемент, который нужно найти.

  Returns:
    Индекс первого вхождения элемента в список, или None, если элемент не найден.
  """

  try:
    return items_list.index(item)
  except ValueError:
    return None

# Пример использования:
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")