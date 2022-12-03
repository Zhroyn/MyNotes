package deque;

public class ArrayDeque<T> {

    private int RFACTOR = 2;
    private int nextFirst;
    private int nextLast;
    private int size;
    private T[] items;

    public ArrayDeque() {
        RFACTOR = 2;
        nextFirst = 7;
        nextLast = 0;
        size = 0;
        items = (T[]) new Object[8];
    }
    public boolean isEmpty() {
        if (size == 0) {
            return true;
        } else {
            return false;
        }
    }
    public int size() {
        return size;
    }
    public T get(int index) {
        if (index < 0 || index >= size) {
            return null;
        }
        return items[(nextFirst + index + 1) % items.length];
    }
    public void resize(int newSize) {
        T[] newArr = (T[]) new Object[newSize];
        for (int i = 0; i < size; i++) {
            newArr[i] = get(i);
        }
        items = newArr;
        nextFirst = newSize - 1;
        nextLast = size;
    }
    public void addFirst(T item) {
        if (size == items.length) {
            resize(size * RFACTOR);
        }
        items[nextFirst] = item;
        nextFirst = (nextFirst + items.length - 1) % items.length;
        size++;
    }
    public void addLast(T item) {
        if (size == items.length) {
            resize(size * RFACTOR);
        }
        items[nextLast] = item;
        nextLast = (nextLast + items.length + 1) % items.length;
        size++;
    }
    public T removeFirst() {
        if (size == 0) {
            return null;
        }
        if (items.length >= 16 && (double)(size - 1) / items.length < 0.25) {
            resize(items.length / RFACTOR);
        }
        nextFirst = (nextFirst + items.length + 1) % items.length;
        size--;
        return items[nextFirst];
    }
    public T removeLast() {
        if (size == 0) {
            return null;
        }
        if (items.length >= 16 && (double)(size - 1) / items.length < 0.25) {
            resize(items.length / RFACTOR);
        }
        nextLast = (nextLast + items.length - 1) % items.length;
        size--;
        return items[nextLast];
    }
    public void printDeque() {
        for (int i = 0; i < size; i++) {
            System.out.print(get(i) + " ");
        }
    }
    public boolean equals(Object o) {
        boolean tag = true;
        if (o instanceof ArrayDeque<?> && ((ArrayDeque<?>) o).size == this.size) {
            for (int i = 0; i < size; i++) {
                if (!((ArrayDeque<?>) o).get(i).equals(this.get(i))) {
                    tag = false;
                    break;
                }
            }
        } else {
            tag = false;
        }
        return tag;
    }
}