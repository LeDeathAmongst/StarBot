# s.hash
Various hashing commands<br/>
 - Usage: `s.hash`
## s.hash md5
MD5 Hash some Text<br/>
 - Usage: `s.hash md5 <txt>`
Extended Arg Info
> ### txt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.hash sha256
SHA256 Hash some Text<br/>
 - Usage: `s.hash sha256 <txt>`
Extended Arg Info
> ### txt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.hash sha512
SHA512 Hash some Text<br/>
 - Usage: `s.hash sha512 <txt>`
Extended Arg Info
> ### txt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.hash sha1
SHA1 Hash some Text<br/>
 - Usage: `s.hash sha1 <txt>`
Extended Arg Info
> ### txt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.encode
Encode a string.<br/>
 - Usage: `s.encode`
## s.encode b16
Encode text into base 16<br/>
 - Usage: `s.encode b16 <message>`
 - Aliases: `base16`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.encode binary
Encode text into binary sequences of 8<br/>
 - Usage: `s.encode binary <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.encode hex
Encode text into hexadecimal<br/>
 - Usage: `s.encode hex <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.encode b64
Encode text into base 64<br/>
 - Usage: `s.encode b64 <message>`
 - Aliases: `base64`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.encode chr
Encode message into character numbers<br/>
 - Usage: `s.encode chr <message>`
 - Aliases: `character`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.encode dna
Encodes a string into DNA 4 byte ACGT format<br/>
 - Usage: `s.encode dna <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.encode rot
Encode a caeser cipher message with specified key<br/>
 - Usage: `s.encode rot <rot_key> <message>`
 - Aliases: `caeser`
Extended Arg Info
> ### rot_key: Optional[int]
> ```
> A number without decimal places.
> ```
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.encode b32
Encode text into base 32<br/>
 - Usage: `s.encode b32 <message>`
 - Aliases: `base32`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.encode braille
Encode text into braille unicode characters<br/>
 - Usage: `s.encode braille <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.decode
Decode a string.<br/>
 - Usage: `s.decode`
## s.decode b64
Decode base 64 text<br/>
 - Usage: `s.decode b64 <message>`
 - Aliases: `base64`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.decode hex
Decode a hexadecimal sequence to text<br/>
 - Usage: `s.decode hex <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.decode b16
Decode base16 text<br/>
 - Usage: `s.decode b16 <message>`
 - Aliases: `base16`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.decode braille
Decide braille unicode characters to ascii<br/>
 - Usage: `s.decode braille <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.decode binary
Decode binary sequences of 8<br/>
 - Usage: `s.decode binary <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.decode b32
Decode base32 text<br/>
 - Usage: `s.decode b32 <message>`
 - Aliases: `base32`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.decode chr
Decode character numbers to a message<br/>
 - Usage: `s.decode chr <message>`
 - Aliases: `character`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.decode dna
Decodes a string of DNA in 4 byte ACGT format.<br/>
 - Usage: `s.decode dna <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.decode rot
Decode a caeser cipher message with specified key<br/>
 - Usage: `s.decode rot <rot_key> <message>`
 - Aliases: `caeser`
Extended Arg Info
> ### rot_key: Optional[int]
> ```
> A number without decimal places.
> ```
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
