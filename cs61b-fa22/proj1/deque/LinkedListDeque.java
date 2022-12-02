package deque;

public class LinkedListDeque<T> {

    private int size;
    private TNode sentinel;

    public class TNode {
        public T item;
        public TNode next;
        public TNode prev;

        public TNode(T i) {
            item = i;
            next = null;
            prev = null;
        }
    }

    public LinkedListDeque() {
        size = 0;
        sentinel = new TNode(null);
        sentinel.next = sentinel;
        sentinel.prev = sentinel;
    }
    public void addFirst(T item) {
        size++;
        TNode newT = new TNode(item);
        newT.next = sentinel.next;
        newT.prev = sentinel;
        newT.next.prev = newT;
        newT.prev.next = newT;
    }
    public void addLast(T item) {
        size++;
        TNode newT = new TNode(item);
        newT.next = sentinel;
        newT.prev = sentinel.prev;
        newT.next.prev = newT;
        newT.prev.next = newT;
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
    public void printDeque() {
        TNode p = sentinel.next;
        while (p != sentinel) {
            System.out.print(p.item + " ");
            p = p.next;
        }
        System.out.print("\n");
    }
    public T removeFirst() {
        if (size == 0) {
            return null;
        } else {
            size--;
            TNode first = sentinel.next;
            first.next.prev = first.prev;
            first.prev.next = first.next;
            return first.item;
        }
    }
    public T removeLast() {
        if (size == 0) {
            return null;
        } else {
            size--;
            TNode last = sentinel.prev;
            last.next.prev = last.prev;
            last.prev.next = last.next;
            return last.item;
        }
    }
    public T get(int index) {
        if (index < 0 || index >= size) {
            return null;
        } else {
            TNode p = sentinel.next;
            for(int i = 0; i < index; i++) {
                p = p.next;
            }
            return p.item;
        }
    }
    public boolean equals(Object o) {
        boolean tag = true;
        if (o instanceof LinkedListDeque<?> && ((LinkedListDeque<?>) o).size == this.size) {
            for (int i = 0; i < size; i++) {
                if (!((LinkedListDeque<?>) o).get(i).equals(this.get(i))) {
                    tag = false;
                    break;
                }
            }
        } else {
            tag = false;
        }
        return tag;
    }

    public T getRecursiveT(TNode p, int index) {
        if (index == 0) {
            return p.item;
        } else {
            return getRecursiveT(p.next, index - 1);
        }
    }
    public T getRecursive(int index) {
        if (index < 0 || index >= size) {
            return null;
        }
        TNode p = sentinel.next;
        return getRecursiveT(p, index);
    }
}