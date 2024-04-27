rule MalwareScanner{
    meta:
        date="27-04-2024"
        tags="Detecting Nimda malware"
    strings:
        $a="0x00409a17"
        $b="0x004029e6"
        $c="0x935F"
        $d="0x0"
        $e={2e 74}
        $f= {5C 2D 2D 20 62 79 74 65 73 20 77 72 69 74 74 65 6E 3A}
        $g={4d 5a}
    condition:
        any of them
}