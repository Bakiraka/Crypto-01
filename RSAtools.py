import random
import binascii
class RSAtools :
    petitspremiers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021]
    def __init__(self):
        pass
    ''' genere une clé RSA de tailles length bits'''
    def generateRSAkey (self, length) :
        """ retourne des cles RSA de la forme n,e,d"""
        firstPrime = self.randomPrime(length)
        secondPrime = self.randomPrime(length)
        n = firstPrime * secondPrime
        e = pow(2,16) + 1
        pgcd = self.xgcd((firstPrime - 1) * (secondPrime - 1), e)
        d = pgcd [2]
        if d < 0 :
            d = d + (firstPrime - 1) * (secondPrime - 1)
        return n,e,d
    
    def randomPrime (self, length) :
        test = False
        while not(test) :
            r = random.getrandbits(length)
            r = (0x1 << (length - 1)) | r | 0x1
            test = self.isPrime(r)
        return r
    def isPrime(self, number) :
        """ retourne True si le nombre est premier (quasiment), False sinon"""
        if number == 2 :
            return True
        if number % 2 == 0 :
            return False
        return self.testPrime(number)
    def testPrime(self, x):
        return self._millerRabin(x)
        """a = 42
        return (pow(a,x,x) == (a % x))"""
    def _millerRabin(self,n,k=20):
            """Test de primalité probabiliste de Miller-Rabin"""
            global petitspremiers
 
            """éliminer le cas des petits nombres <=1024"""
            if n<=1024:
                if n in petitspremiers:
                    return True
                else:
                    return False
                """recommencer le test k fois: seul les nb ayant réussi k fois seront True"""
            for repete in range(0, k):
                """trouver un nombre au hasard entre 1 et n-1 (bornes inclues)"""
                a = random.randint(1, n-1)
                """si le test echoue une seule fois => n est composé"""
                if not self.millerRabin(a, n):
                    return False
            """ n a réussi les k tests => il est probablement 1er"""
            return True
        
    def millerRabin(self, a, n) :
        """Ne pas appeler directement (fonction utilitaire). Appeler millerRabin(n, k=20)"""
        """trouver s et d pour transformer n-1 en (2**s)*d"""
        d = n - 1
        s = 0
        while d % 2 == 0:
            d >>= 1
            s += 1
            
        """expentiation modulaire (a**d)%n"""
        apow = pow(a,d,n)
 
        """ si (a**d) % n ==1 => n est probablement 1er"""
        if apow == 1:
            return True
 
        for r in range(0,s):
            """ si a**(d*(2**r)) % n == (n-1) => n est probablement 1er """
            if pow(a,d,n) == n-1:
                return True
            d *= 2
 
        return False

    def xgcd(self, a,b):
        """Extended GCD:
        Returns (gcd, x, y) where gcd is the greatest common divisor of a and b
        with the sign of b if b is nonzero, and with the sign of a if b is 0.
        The numbers x,y are such that gcd = ax+by."""
        prevx, x = 1, 0;  prevy, y = 0, 1
        while b:
            q, r = divmod(a,b)
            x, prevx = prevx - q*x, x  
            y, prevy = prevy - q*y, y
            a, b = b, r
        return a, prevx, prevy

    def encrypt(self, pk, msg):
        return pow(msg, pk [1], pk [0])

    def decrypt(self, sk, cipher):
        return pow(cipher, sk [1], sk [0])
    '''encrypte une chaine de caractere avec RSA'''
    def encrypt_str(self, pk, msg):
        x = binascii.hexlify(msg.encode('UTF-8'))
        msgint = int(x,16)
        return self.encrypt(pk, msgint)
    ''' decrypte une chaine de caractere avec RSA '''
    def decrypt_str(self, sk, cipher):
        decrypt = self.decrypt(sk, cipher)
        decrypthex = hex(decrypt) [2:]
        y = binascii.unhexlify(decrypthex)
        decryptstr = str(y,'UTF-8')
        return decryptstr
    def str_to_key (self, string) :
        return string.split()
        return accu
    ''' encrypte un nombre de n bits en le découpant par bloc '''
    def cryptblock (self, sk, message) :
        tmp = message 
        listmess = []
        while (tmp > 0) :
            '''tmp2 contient les lsb'''
            tmp2 = tmp & 0xFFFFFFFFFFFFFFFF
            ''' on décale tmp afin de récuperer tout les bits '''
            tmp = tmp >> 64
            ''' on crypte les lsb de tmp et on le stocke dans la liste '''
            decrypt = self.encrypt(sk, tmp2)
            listmess.append(decrypt)
        return listmess
    ''' decrypt un nombre de n bits en decryptant les block puis en les fusionnant '''
    def decryptblock(self, pk, message) :
        accu = 0x0
        j = 0
        for i in message :
            ''' on decrypte le bloc actuelle '''
            tmp = self.encrypt(pk,i)
            ''' on met le bloc a sa place '''
            tmp = tmp << (64 * j)
            ''' on fusionne le block decrypt avec l'accumulateur'''
            accu = accu | tmp
            j = j + 1
        return accu
