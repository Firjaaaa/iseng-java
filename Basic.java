public class Basic {

    // jadi ini mungkin topik pertama yang bakalan gua pelajari dalam bahasa java
    // adalah variable. dalam bahasa java ini agak unik sih menurut gua, karna beda
    // banget pendeklarasian sebuah variable dengan bahasa pemoggraman python.
    // dipython kita tidak perlu mendeklarasikan type variable apa yang mau kita
    // deklarasikan, sedangkan di java ini wajib untuk dideklarasikan terlebih
    // dahulu. kalau kita tidak deklarasikan = Error

    String untukBanyakHuruf = "Wajib pakain double quetes kalau hurufnya lebih dari 1";
    int untukWholeNumbers = 12;
    double untukAngkaDesimal = 19.0;
    boolean hanyaAdaTrueOrFalse = true;
    char iniCumanBisa1Angka = 'p';
    final String fungsiFinal = "fungsi final sebelum type data string adalah agar value dalam variable tidak bisa diubah/ditimpa dengan yang baru(ditimpa dengan kode yang akan mendatang)";

    // print method biasanya digunakan untuk menampilkan value/isi variable ke
    // terminal. untuk menggabungkan variable kita biasanya menggunakan tanda +.
    // ketika kedua variable string ditambahkan dengan +, makan kedua kalimat
    // tersebut akan tergabung menjadi 1 paragraf. akan tetapi ketika type data
    // string ditambahkan dengan int, makan int itu akan menjadi tipe data string
    // karna dia akan bergabung kedalam paragraf string. kalau kedua tipe datanya
    // int, maka akan berjalan seperti operasi penjumlahan mtk pada umumnya. hati
    // hati jika kita menjumlahkan dua tipe integer + satu tipe string. karna rawan
    // terjadi miss logika hanya karna lupa sama aturan PEMDAS pada mtk. jadi
    // alangkah baiknya ketika menambahkan dua tipe integer atau lebih dengan
    // string, alangkah baiknya kita kasih tanda kurung terlebih dahulu agar
    // dieksekusi pertama kali ().

    public static void main(String[] args) {
    System.out.println("Jumlahnya adalah " + 5 + 6);
    // // kode diatas berbeda dengan kode dibawah secara jumlah
    System.out.println("Jumlahnya adalah " + (5 + 6));
    // hal ini disebabkan karna pengoperasian mtk adalah dari kiri ke kanan
    // berdasarkan aturan PEMDAS. jadi kenapa jumlahnya bisa beda karna kode baris
    // pertama itu mengubah 5 menjadi string, otomatis penjumlahan 5 + 6 tidak akan
    // berjalan dengan normal, karna angka 5 sudah menjadi string terlebih dahulu.
    // oleh karna itu make sure untuk selalu ngasih tanda kurung terhadap
    // penjumlahan angka kalau ingin menggabungkan dengan type data selain data
    // }

    public static void main(String[] args) {
        String nama = "udin";
        int umurNama = 18;
        boolean statusHidup = true;
        System.out.println("Nama: " + nama + " Umur: " + umurNama + " Status Hidup: "
                + statusHidup);
    }

    // penamaan dalam java. didalam java normalnya menggunakan style cammelCase,
    // yaitu huruf kecil diawal lalu huruf besar saat berganti kata. perlu diingat
    // didalam penamaan variable dilarang menggunakan spasi dan diawali dengan
    // sebuah angka. penamaan variable juga sangat sensitive sifatnya terhadap huruf
    // besar dan huruf kecil. furinaMyBini dengan furinamybini adalah dua variable
    // yang berbeda didalam java. kita juga tidak boleh menggunakan nama built in
    // alias syntax java sebagai nama variable. contoh:
    // String int = "furina cantik banget"; maka akan ERROR

    public static void main(String[] Args) {
        String namaIstriFirja = "Furina";
        int umurIstriFirja = 500;
        String sikapIstriFirja = "Lucu, Periang, Extrovert";
        boolean statusPernikahan = true;
        System.out.println("========================================================");
        System.out.println("=    Nama Istri firja = " + namaIstriFirja + "                         =");
        System.out.println("=    Umur Istri Firja = " + umurIstriFirja + "                            =");
        System.out.println("=    Sikap Istri firja = " + sikapIstriFirja + "      =");
        System.out.println("=    Status Pernikahan = " + statusPernikahan + "                          =");
        System.out.println("========================================================");

    }

}
