package com.cyao.theconverter.worlds;

import kotlin.Metadata;
import kotlin.jvm.internal.Intrinsics;
import kotlin.text.Regex;

@Metadata(mo3720d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\u0018\u00002\u00020\u0001B\r\u0012\u0006\u0010\u0002\u001a\u00020\u0003¢\u0006\u0002\u0010\u0004J\u0006\u0010\u0007\u001a\u00020\u0003R\u0011\u0010\u0002\u001a\u00020\u0003¢\u0006\b\n\u0000\u001a\u0004\b\u0005\u0010\u0006¨\u0006\b"}, mo3721d2 = {"Lcom/cyao/theconverter/worlds/jurassic;", "", "last", "", "(Ljava/lang/String;)V", "getLast", "()Ljava/lang/String;", "jurassic1", "app_debug"}, mo3722k = 1, mo3723mv = {1, 6, 0}, mo3725xi = 48)
/* compiled from: jurassic.kt */
public final class jurassic {
    private final String last;

    public jurassic(String last2) {
        Intrinsics.checkNotNullParameter(last2, "last");
        this.last = last2;
    }

    public final String getLast() {
        return this.last;
    }

    public final String jurassic1() {
        Regex regex = new Regex("\\s*\\(dino" + "@ZombieTypes" + "\\)\\s*");
        Regex regex2 = new Regex("\\s*\\(dino_armor1" + "@ZombieTypes" + "\\)\\s*");
        Regex regex3 = new Regex("\\s*\\(dino_armor2" + "@ZombieTypes" + "\\)\\s*");
        Regex regex4 = new Regex("\\s*\\(dino_armor3" + "@ZombieTypes" + "\\)\\s*");
        Regex regex5 = new Regex("\\s*\\(dino_armor4" + "@ZombieTypes" + "\\)\\s*");
        Regex regex6 = new Regex("\\s*\\(dino_bully" + "@ZombieTypes" + "\\)\\s*");
        Regex regex7 = new Regex("\\s*\\(dino_bully_veteran" + "@ZombieTypes" + "\\)\\s*");
        Regex regex8 = new Regex("\\s*\\(dino_gargantuar" + "@ZombieTypes" + "\\)\\s*");
        Regex regex9 = new Regex("\\s*\\(dino_imp" + "@ZombieTypes" + "\\)\\s*");
        return new Regex("\\s*\\(modern_superfanimp" + "@ZombieTypes" + "\\)\\s*").replace((CharSequence) regex9.replace((CharSequence) regex8.replace((CharSequence) regex7.replace((CharSequence) regex6.replace((CharSequence) regex5.replace((CharSequence) regex4.replace((CharSequence) regex3.replace((CharSequence) regex2.replace((CharSequence) regex.replace((CharSequence) this.last, "96 \\{\\{P|Jurassic Zombie|2}}"), "97 \\{\\{P|Jurassic Conehead|2}}"), "98 \\{\\{P|Jurassic Buckethead|2}}"), "99 \\{\\{P|Jurassic Fossilhead|2}}"), "100 \\{\\{P|Amberhead Zombie|2}}"), "103 \\{\\{P|Jurassic Bully|2}}"), "103 \\{\\{P|Jurassic Bully|2}}"), "101 \\{\\{P|Jurassic Gargantuar|2}}"), "102 \\{\\{P|Jurassic Imp|2}}"), "104 \\{\\{P|Flint imp|2}}");
    }
}
