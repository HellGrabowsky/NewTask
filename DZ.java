import java.util.*;

public class PhoneBook {
    private HashMap<String, TreeSet<String>> contacts;

    public PhoneBook() {
        contacts = new HashMap<>();
    }

    public void addContact(String name, String phoneNumber) {
        TreeSet<String> phoneNumbers = contacts.getOrDefault(name, new TreeSet<>());
        phoneNumbers.add(phoneNumber);
        contacts.put(name, phoneNumbers);
    }

    public void displayContacts() {
        // Создаем список записей с количеством телефонов для каждого контакта
        List<Map.Entry<String, TreeSet<String>>> sortedContacts = new ArrayList<>(contacts.entrySet());
        sortedContacts.sort((c1, c2) -> c2.getValue().size() - c1.getValue().size());

        // Выводим отсортированные записи
        for (Map.Entry<String, TreeSet<String>> entry : sortedContacts) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    public static void main(String[] args) {
        PhoneBook phoneBook = new PhoneBook();

        // Добавляем контакты
        phoneBook.addContact("John", "1234567890");
        phoneBook.addContact("John", "0987654321");
        phoneBook.addContact("Alice", "1112223333");
        phoneBook.addContact("Bob", "4445556666");
        phoneBook.addContact("Alice", "9998887777");

        // Выводим контакты
        phoneBook.displayContacts();
    }
}
